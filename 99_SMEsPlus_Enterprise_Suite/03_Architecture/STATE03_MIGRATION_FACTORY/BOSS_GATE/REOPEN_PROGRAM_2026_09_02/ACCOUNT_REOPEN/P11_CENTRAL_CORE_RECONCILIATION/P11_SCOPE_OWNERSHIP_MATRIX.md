# P11 — UNIFIED SCOPE OWNERSHIP MATRIX

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Created under controlled constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`.
**Correction applied in-flight. No reset. No evidence discarded. No completed work repeated.**

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. What the correction changed, stated precisely

**Superseded:** any wording implying *"Tenant Context + Company Context are mandatory for every
operation."*

**Canonical:** `SCOPE-AWARE EVERYWHERE.` Every material object, operation, access path, financial
event, configuration, reference, report and mutation **first determines its applicable scope**, then
carries only the context that scope requires.

| Scope | Tenant context | Company context |
|---|---|---|
| `PLATFORM` | not required | not required |
| `TENANT` | **mandatory** | not required unless the specific operation is company-scoped |
| `COMPANY` | **mandatory** | **mandatory** |

`MISSING REQUIRED SCOPE = DENY.` `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY.`

`TENANT` = security / customer boundary. `COMPANY` = legal / accounting / business boundary.
`OWNERSHIP ≠ AVAILABILITY.` `OWNERSHIP SCOPE ≠ OPERATIONAL SCOPE ≠ FINANCIAL SCOPE ≠ REFERENCE SCOPE.`
`MULTI-TENANT MEMBERSHIP ≠ MULTI-TENANT EXECUTION CONTEXT.`
`UNRELATED INDEPENDENT COMPANIES = SEPARATE TENANTS BY DEFAULT.`

---

## 2. The finding the correction produces — stated before the matrix

> ## The reference model does not under-scope. It **fails to declare scope at all**.
>
> Wave A `16` established that **no tenant concept exists** and the outermost boundary is the company
> group. Under the corrected constitution that fact is re-read, and the re-reading is sharper than the
> original:
>
> **The defect is not "objects are missing a company or tenant field."** It is that **no object
> declares which of the three scopes it belongs to**, so a reviewer cannot distinguish
>
> - a **legitimate** `PLATFORM`-scoped read that correctly bypasses every company record rule, from
> - an **isolation breach** — a `TENANT`- or `COMPANY`-scoped object read without its required context.
>
> **Both look identical in the evidence.** That is why `T0-07` — *cross-company rate resolution
> outside every record rule* — could be widened four times across four rounds and never resolved: the
> rounds were arguing about severity when the missing datum was the object's declared scope.

`P11-DERIVED, SUPPORTED INTERPRETATION.` It does **not** resolve `T0-07`; it explains why `T0-07` is
not resolvable by further source reading, which is what `SL-01`'s tolerance-zero register independently
concluded by a different route (*"none of the twelve is closable by more source reading alone"*).

---

## 3. Scope determination — the eight questions, answered per material object

Per correction §4. `?` marks a determination the evidence does not support; those become
`HOLD — SCOPE EVIDENCE REQUIRED`.

| Object | Owns | Executes | Access | Mutate | Reference | Financial effect? | Company owning the effect | Data class |
|---|---|---|---|---|---|---|---|---|
| Chart-of-accounts **standard template** | `PLATFORM` | `PLATFORM` | `TENANT` | `PLATFORM` | `TENANT` | no | — | platform reference |
| Chart-of-accounts **tenant/company instance** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no directly | — | company legal truth |
| **Journal** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | enabling | its own | company legal truth |
| **Journal entry / item** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` (immutable once posted) | `COMPANY` | **yes** | its own | company legal truth |
| **Accounting event** *(to be introduced — `UAE-29`)* | `COMPANY` | `COMPANY` | `COMPANY` | never | `COMPANY` | **yes** | its own | company legal truth |
| **Settlement / matching record** | `COMPANY` | `COMPANY` | `COMPANY` | never | `COMPANY` | **yes** | its own | company legal truth |
| **Currency definition** (ISO currency) | `PLATFORM` | `PLATFORM` | `TENANT` | `PLATFORM` | `COMPANY` | no | — | platform reference |
| **FX rate observation** (a market rate on a date) | `PLATFORM` **candidate** | `PLATFORM` | `TENANT` | `PLATFORM` | `COMPANY` | no | — | platform reference |
| **FX rate *selection* for a transaction** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | — | **yes** | its own | company legal truth |
| **Fiscal year / period definition** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no directly | — | company legal truth |
| **Lock date / finality declaration** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes** (gates recognition) | its own | company legal truth |
| **Lock exception grant** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | — | **yes** | its own | company legal truth |
| **Numbering / date-alignment control parameter** | `TENANT` **at minimum** | `COMPANY` | `TENANT` | `TENANT` | — | **yes** — it moves accounting dates | the company it acts on | **scope-mismatched today** |
| **Tax rate / statutory reference** (Thai VAT, WHT rates) | `PLATFORM` **candidate** | `PLATFORM` | `TENANT` | `PLATFORM` | `COMPANY` | no | — | platform reference |
| **Tax configuration** (which tax applies to what) | `TENANT` **or** `COMPANY` — `?` | `COMPANY` | `COMPANY` | `?` | `COMPANY` | **yes** | its own | `HOLD — SCOPE EVIDENCE REQUIRED` |
| **Product master** | `TENANT` (per Boss ruling `D-01`) | `COMPANY` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| **Costing method** (on the product category) | `COMPANY` — *company-scoped property of the category* | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes** | its own | company legal truth |
| **Stock quantity / location** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `TENANT` (visibility) | no | — | company operational truth |
| **Stock valuation layer** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes** | its own | company legal truth |
| **Asset record** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes** | its own | company legal truth |
| **Equipment / machine record** | `COMPANY` — `?` *(`CTR-C-10`: records with an empty company exist)* | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes**, via absorption | `?` | `HOLD — SCOPE EVIDENCE REQUIRED` |
| **Work centre & its hourly rate** | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | **yes** | its own | company legal truth |
| **Normal capacity** *(to be introduced)* | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | — | **yes** | its own | company legal truth |
| **Analytic / management dimension definition** | `TENANT` | `COMPANY` | `TENANT` | `TENANT` | `COMPANY` | no | — | tenant-owned |
| **Analytic line (derived)** | `COMPANY` | `COMPANY` | `COMPANY` | derived only | `TENANT` (reporting) | no | — | company derived |
| **Budget** | `TENANT` **or** `COMPANY` — `?` | `COMPANY` | `TENANT` | `TENANT` | — | **no — budget consumes the ledger** | — | tenant-owned |
| **Report definition — standard** | `PLATFORM` | `TENANT` | `TENANT` | `PLATFORM` | — | no | — | platform reference |
| **Report definition — tenant-authored** | `TENANT` | `TENANT` | `TENANT` | `TENANT` | — | no | — | tenant-owned |
| **Financial statement output** | `COMPANY` | `COMPANY` | `COMPANY` | never | `TENANT` (consolidation) | no | — | company legal truth |
| **Integrity hash chain** | `COMPANY` | `COMPANY` | `COMPANY` | never | — | **yes** (assurance) | its own | company legal truth |
| **Control / deletion evidence** | `TENANT` at minimum | `COMPANY` | `TENANT` | never | — | **yes** (assurance) | the acting company | **scope-mismatched today** |
| **Migration / replay batch** | `TENANT` | `COMPANY` | `TENANT` | `TENANT` | `COMPANY` | **yes** | each affected company | `HOLD` — does not exist (`GAP-FS-08`) |

**Two `HOLD — SCOPE EVIDENCE REQUIRED`** *(~~Four~~ → **three** per `X4-F11`, → **two** per `X3-F09` and Delta 02; superseded values retained so erasure is detectable)*: ~~tax configuration~~ resolved `COMPANY`; ~~equipment/machine ownership~~ resolved `TENANT` conditionally (`P11-F-05`); **budget**;
and migration/replay batch (which does not exist at all). Each is recorded in
`P11_FINAL_BLOCKER_REGISTER.md`.

---

## 4. Scope-mismatch register — where the object's scope and its store's scope disagree

This is the corrected form of what the inherited packages recorded as "missing company dimension".

| id | Object | Correct scope | Scope actually available in the store | Consequence | Inherited id |
|---|---|---|---|---|---|
| `SC-01` | Numbering / date-alignment control | `TENANT` at minimum; it moves accounting dates | **no dimension at all — database-wide** | **One write disables a control for every tenant in the database, invisibly.** Highest severity in the inherited base | `SB-01`, `COR-16` |
| `SC-02` | Report definition | two different scopes (`PLATFORM` standard, `TENANT` authored) sharing one model | **one undifferentiated model, no record rule, full create/write/unlink for the accounting-manager role** | Platform reference data and tenant-authored data are **indistinguishable and share one permission**. This is the corrected statement of `MCU-04` | `MCU-04` `CLOSED — VERIFIED DEFECT`; `FC-A1` |
| `SC-03` | Menu created by a report action | `TENANT` | **no company field, no record rule** | A menu created by one company's manager is visible to every holder of the group, in every company | `FC-A1` |
| `SC-04` | Fiscal year | `COMPANY` — it is a legal/accounting boundary | **root companies only; child companies refused** | A company cannot declare its own legal period. **Under the corrected model this is a scope violation, not a convenience limit** | `COR-01` |
| `SC-05` | FX rate table | `PLATFORM` for the observation, `COMPANY` for the selection | **one table keyed to the company-group root** | The two scopes are collapsed into one object, which is precisely why the resolution behaviour cannot be classified as legitimate or as a breach | `T0-07`, `EV-018`, `GB-08` |
| `SC-06` | Per-company account code | `COMPANY` | keyed to the **root company**, encoded as `account × 10000 + company` | Aliases silently once any company identifier reaches 10,000 | `SB-02`, `COR-18` |
| `SC-07` | Integrity hash chain | `COMPANY`, keyed on business identity | keyed on **storage row identifiers** | Cannot survive a tenant split, merge, restore or migration | `SB-03`, `COR-12` |
| `SC-08` | Control / deletion evidence | `TENANT` — it is the tenant's own record | **the application log** | Leaves the tenant's data entirely; in shared infrastructure it is neither tenant-scoped nor tenant-accessible | `SB-04` |
| `SC-09` | Hard lock cascade | `COMPANY`, within one tenant | cascades from **every** parent, irreversibly | Couples entities a tenant may consider independent. **Materially narrowed by the correction** — see §5 | `EV-008`, `CL-05` |

---

## 5. Revalidation — findings materially affected by the superseded assumption

Per correction §6. **Only** findings that used the Tenant+Company-everywhere assumption are revisited.
Everything else is preserved unchanged.

### `RV-01` — Wave A `TI-01`

| | |
|---|---|
| **Original finding** | *"Every control-affecting configuration value carries a tenant dimension. **No configuration may have database-wide effect.**"* |
| **Scope assumption used** | Tenant context mandatory for every configuration object |
| **Why over-constrained** | `PLATFORM`-scoped reference data — an ISO currency, a statutory tax rate, a standard report definition — **legitimately** has platform-wide effect. A blanket prohibition would forbid the platform layer from existing |
| **Correct scope analysis** | The defect in `SB-01` is **not** that the store lacks a tenant dimension. It is that a **`TENANT`-scoped control is held in a `PLATFORM`-scoped store**, and nothing declares which it is |
| **Updated classification** | `TI-01` restated as: *every configuration object declares its scope; a `TENANT`- or `COMPANY`-scoped value may not be held in a store of wider scope.* `SC-01` **severity unchanged — highest** |
| **Architecture impact** | The platform layer is now expressible. `TI-01`'s intent is preserved and its reach corrected |
| **Cross-process impact** | `P07` benefits most — statutory tax reference is `PLATFORM` and no longer needs an artificial tenant dimension |
| **Evidence required** | none — this is a constitutional determination |

### `RV-02` — `MCU-04` / `account.report`

| | |
|---|---|
| **Original finding** | *"`account.report` has **no company dimension**"* — read as a defect in itself |
| **Scope assumption used** | Every object requires a company dimension |
| **Why over-constrained** | A **standard** report definition is `PLATFORM` reference data, for which absence of a company dimension is **correct by design** |
| **Correct scope analysis** | The verified defect **survives and sharpens**: one undifferentiated model serves two scopes, carries **no record rule in any of 6 roots**, and grants **full create/write/unlink** to the accounting-manager role. A tenant-authored report is `TENANT`-scoped and is stored as though it were platform reference data |
| **Updated classification** | `MCU-04` remains **`CLOSED — VERIFIED DEFECT`**. Its *statement* is corrected; its *disposition* is unchanged. `SC-02` |
| **Architecture impact** | The remedy changes: **not** "add a company field" but "declare the scope and split the permission." Adding a company field to a platform-scoped object would have been the wrong fix |
| **Cross-process impact** | `P08`/`P09` reporting; and it is the same defect as Boss question 16 (*standard vs tenant-specific — no distinction exists*), now seen to be **one defect with two instances**, not two |
| **Evidence required** | none for the mechanism; `MCU-22` (record rule in the 16 unsearched roots) remains **`NON-GATING`** |

### `RV-03` — `T0-07` cross-company rate resolution

| | |
|---|---|
| **Original finding** | Rate resolution occurs **outside every record rule**, with undeclared fallbacks — read as a cross-company isolation breach |
| **Scope assumption used** | Any read bypassing company record rules is a breach |
| **Why over-constrained** | If the FX rate **observation** is `PLATFORM` reference data, bypassing company record rules to read it is **correct**, not a breach |
| **Correct scope analysis** | The object conflates two scopes (`SC-05`). The **selection** of a rate for a company's transaction is `COMPANY`-scoped and produces a financial effect; the **observation** is not. The evidence cannot separate them because the model does not |
| **Updated classification** | **`T0-07` remains `UNRESOLVED`. Tolerance-zero. Not weakened, not narrowed, not conditionally passed.** What changes is the *reason it is unresolvable by source reading*: the scope declaration is missing, not the record rule |
| **Architecture impact** | `GB-08` gains a fourth framing: the rate-resolution question is a **scope-declaration** question before it is a version question |
| **Cross-process impact** | `P06`, `P07`, `P08`; every monetary display |
| **Evidence required** | Unchanged — `MCU-19` needs a database; `MCU-01`/`MCU-20` need a running instance |

### `RV-04` — hard lock cascade / `CL-05`

| | |
|---|---|
| **Original finding** | A parent's irreversible lock cascading to subsidiaries *"couples entities a tenant may consider independent"* |
| **Scope assumption used** | Company hierarchy and tenant boundary are independent axes |
| **Why over-constrained** | The correction states `UNRELATED INDEPENDENT COMPANIES = SEPARATE TENANTS BY DEFAULT` |
| **Correct scope analysis** | Genuinely unrelated companies are **separate tenants**, so no cascade can reach them. The residual risk is confined to **related companies inside one tenant** — real, but materially narrower |
| **Updated classification** | `SC-09` **narrowed**. `CL-05` remains a decision; its blast radius is reduced from *"any two companies"* to *"a parent and its children inside one tenant"* |
| **Architecture impact** | The tenant boundary becomes the outer guarantee; the company hierarchy is an inner policy |
| **Cross-process impact** | `P08` close; `DC-13` cross-company leakage narrowed |
| **Evidence required** | none |

### `RV-05` — handoff contract element 10

| | |
|---|---|
| **Original finding** | `BC-02` element 10 reads *"`WHICH Company / Tenant` — **mandatory** company and tenant context"*, and `SL-07` `16` §3.1 reports it failing on **10 of 10** material handoffs |
| **Scope assumption used** | Both contexts mandatory on every handoff |
| **Why over-constrained** | **As a general rule for all handoffs, yes** — a `PLATFORM`-scoped handoff would need neither |
| **Correct scope analysis** | **All ten material Inventory→Accounting handoffs create a financial effect.** By the correction's own §5 (*Company Inventory Valuation → COMPANY*) every one of them is `COMPANY`-scoped, and for `COMPANY` scope **both contexts remain mandatory** |
| **Updated classification** | **The 10-of-10 element-10 failure stands, unchanged.** The correction changes the *general* rule and does **not** relieve these ten. `RISK-U03` unchanged |
| **Architecture impact** | Element 10 should be restated as *"the object's declared scope, and every context that scope requires"* — which is stricter in effect, since it also forbids supplying a context the scope does not authorise |
| **Cross-process impact** | The same restatement applies to the generalised contract in `P11_SUBLEDGER_ARCHITECTURE.md` §4 |
| **Evidence required** | none |

> **`RV-05` is the revalidation most likely to have gone the other way.** It is recorded in full
> because a correction that relaxes a rule invites the reading that a failing count relaxes with it.
> **It does not here**, and saying so is the point of running the revalidation rather than assuming
> its direction.

---

## 6. Scope positions P11 asserts

| id | Position | Basis |
|---|---|---|
| `SCP-01` | **Every material object carries a declared scope — `PLATFORM`, `TENANT` or `COMPANY` — as a first-class, non-null property.** Absence of a context field is not evidence of platform scope | `SC-01`…`SC-09` |
| `SCP-02` | **A `TENANT`- or `COMPANY`-scoped value may not be stored in a store of wider scope.** This is the corrected, and sharper, form of `TI-01` | `RV-01` |
| `SCP-03` | **An object that serves two scopes must be two objects.** Report definitions, FX rate tables and chart-of-accounts entries each currently serve two | `SC-02`, `SC-05`, and Boss question 16 |
| `SCP-04` | **Financial effect implies `COMPANY` scope, always.** Any object whose mutation changes a ledger assertion is company-scoped regardless of where it is configured | correction §4 q6–q7 |
| `SCP-05` | **`MISSING REQUIRED SCOPE = DENY` must be enforced at the point of effect, not at the point of entry** — because `UAE-01`…`UAE-09` are emitted by the ledger with no operator request | `P11_UNIFIED_ACCOUNTING_EVENT_REGISTER.md` §2 |
| `SCP-06` | **Control and assurance evidence is `TENANT`-scoped at minimum and lives inside the tenant's own data** | `SC-08` |
