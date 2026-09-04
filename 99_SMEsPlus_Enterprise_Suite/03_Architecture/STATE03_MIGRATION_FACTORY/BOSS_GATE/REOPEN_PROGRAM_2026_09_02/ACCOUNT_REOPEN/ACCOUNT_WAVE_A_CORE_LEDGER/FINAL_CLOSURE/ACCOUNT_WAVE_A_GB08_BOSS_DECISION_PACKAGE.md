# ACCOUNT WAVE A — `GB-08` BOSS DECISION PACKAGE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`

> # `BOSS DECISION REQUIRED — GB-08`
>
> **This file does not select an option. It states the evidence, the consequences and the options.**
> Boss is the sole Final Approver. No implementation, freeze or architecture decision is taken here.

---

## 1. Affected concept, table and semantic

| Element | Value |
|---|---|
| **Concept** | *Which company's exchange-rate rows value a transaction* |
| **Table** | `res_currency_rate` (model `res.currency.rate`) |
| **Semantic under study** | The resolution rule: given an acting company that may be a **branch** of a root, and a rate table whose rows may name a company **or be company-less (`NULL`)**, which row is selected |
| **Why it is Wave A** | Every foreign-currency measurement in the ledger passes through it: initial recognition, unrealised revaluation, realised FX, consolidation, and every monetary aggregate on screen |

---

## 2. Version-by-version evidence

Declared path set for the line-level diffs below — **four trees**, each opened directly.
**This path set is corrected and extended to 22 roots in §2.4; read §2.4 before relying on §2.**

| Tag | Tree | File date |
|---|---|---|
| **V18-A** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server/odoo/addons/base/models/res_currency.py` | 2025-02-23 |
| **V18-B** | `/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605/odoo/addons/base/models/res_currency.py` | 2026-06-05 |
| **V19-A** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/ODOO19/addons/base/models/res_currency.py` | — |
| **V19-B** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/SMEsPlus19/SOURCE CODE /addons/base/models/res_currency.py` | — |

**V19-A and V19-B are byte-identical** (`diff -q` → no difference). The two v19 trees are one datum.

### 2.1 Divergence 1 — branch preference in `_get_conversion_rate`

**V18-A and both v19 trees:**

```python
def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
    if from_currency == to_currency:
        return 1
    company = company or self.env.company
```

**V18-B only:**

```python
def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
    if from_currency == to_currency:
        return 1
    if company == self.env.company.root_id:
        company = self.env.company          # Get rates through branch if selected company
    else:
        company = company or self.env.company
```

Exact machine diff, V18-A → V18-B:

```diff
@@ -266,7 +266,10 @@
     def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
         if from_currency == to_currency:
             return 1
-        company = company or self.env.company
+        if company == self.env.company.root_id:
+            company = self.env.company  # Get rates through branch if selected company
+        else:
+            company = company or self.env.company
```

> **The behaviour is not merely unstable. It is non-monotonic: `absent → present → absent`.**
> It was introduced in a v18 point release and **was not carried forward into v19.**

### 2.2 Divergence 2 — a new rate resolver in the v19 ORM **core**

`SMEsPlus19/odoo-19.0+e.20260312/odoo/orm/models.py:1975–2003`, `_read_group_select`, branch
`func == 'sum_currency'`:

```sql
(SELECT DISTINCT ON (currency_id) currency_id, rate
   FROM "res_currency_rate"
  WHERE company_id IS NULL OR company_id = <env.company.root_id.id>
  ORDER BY currency_id,
           company_id,
           CASE WHEN name <= <today> THEN name END DESC,
           CASE WHEN name >  <today> THEN name END ASC)
```

joined by `query.add_join('LEFT JOIN', …)` and consumed as `SUM(amount / COALESCE(rate, 1.0))`.

Four properties, each verified by inspection of the constructed SQL:

1. **Raw SQL, not `_search`.** Unlike `_get_rates`, which builds its query through `Rate._search(...)`,
   this subquery is written literally. **No record rule is applied to `res.currency.rate`.**
2. **Converts at `Date.context_today(self)`** — *today's* rate, **not the record's date**.
3. **`COALESCE(rate, 1.0)`** — a **silent par fallback**. A missing rate produces a number, not an error.
4. **Scoped to `env.company.root_id`** — the branch's own rows are not preferred; the root's are.

**`sum_currency` does not exist anywhere in v18** (zero occurrences across the whole v18 package).
It is **new in v19**.

*Attribution:* this resolver is already on the record as `MCU-20` / `BW-31` in the parent package. This
round **independently reproduced** it from source; that reproduction is a repeatability datum for
`MC-04`, not a new finding.

### 2.3 Reachability of Divergence 2 — verified, and it is broad

| Emitter | File | Behaviour |
|---|---|---|
| List / relational views | `web/static/src/model/relational_model/utils.js:545–553` | For **every** field with `aggregator && currency_field` — i.e. every monetary field — appends `<field>:sum_currency`. **Opt-out by field definition, not opt-in** |
| Pivot | `web/static/src/views/pivot/pivot_model.js:1088–1090` | same |
| Graph | `web/static/src/views/graph/graph_model.js:337` | same |

**Visible consequence is narrower than reachability.** `utils.js:596–601` and
`pivot_model.js:992–997` **discard** the `sum_currency` value and display the plain sum when the group
spans a **single** currency. The record-rule-bypassing query still **executes** on essentially every
grouped monetary read; the wrong figure **surfaces** only on groups spanning two or more currencies.

### 2.4 The path set was wrong — corrected by mechanical root discovery

**§2's four trees are not the population.** A mechanical discovery over the whole evidence volume —
declared pattern: every directory containing `addons/base/models/res_currency.py` — returns
**22 reference core roots**, not four, and not the one the parent round declared.

**Method validation, stated before the result is used.** Applying this round's manifest count to the
parent round's *own* declared root, `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo`,
returns **1,753** manifested modules. The parent declared **791** (`addons/`) + **961**
(`addons_archive/`) = **1,752**, +1 for the root manifest. **The two counts agree exactly.** The
extension below is therefore a change of path set, not a change of counting method.

`Δ1` was then re-tested across **all 22 roots** on the exact source string
`Get rates through branch if selected company`:

| `Δ1` branch preference | Roots | Which |
|---|---|---|
| **PRESENT** | **5 of 22** | `MIGRATION/ODOO18/18.0.1` · `MIGRATION/ODOO18/18.0.2_community_enterprise` · **`MIGRATION/ODOO18/18.0.3_smeplus`** · `MIGRATION/ODOO18/odoo-18.0.post20260605` · `ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605` |
| **ABSENT** | **17 of 22** | **every v19 root** · every enterprise/community v18 base · **`SMEsPlus18/odoo-18.0+e.20250608` — the parent round's own primary research root** |

Three consequences, each material:

> ### `FC-F2` — the Wave A rate research was executed against a root where `Δ1` is ABSENT, while a root named for SMEsPlus itself has it PRESENT.
>
> `18.0.3_smeplus` — the only root in the universe whose name asserts the SMEsPlus line — **carries the
> branch-preference behaviour.** The parent round's declared source root, `odoo-18.0+e.20250608`,
> **does not.** Every behavioural conclusion in the Wave A rate-table chain is bound to the latter.
> **This does not falsify those conclusions; it bounds them to a root that may not be the target.**

> ### `FC-F3` — `GB-08` is understated. The behaviour is not a single point-release anomaly.
>
> The parent round described *"a later v18 point release"* — **one** tree. It is **five roots across at
> least three distinct v18 lines**, including two independent copies of `post20260605` and three
> `MIGRATION` builds. The instability is a **property of the v18 line**, not an artefact of one build.

> ### `FC-F4` — `GB-07` is confirmed and widened again, on the same axis, at the level above the one it was corrected at.
>
> The parent round's lesson was *"declare the pattern AND prove the path set — and the proof of a path
> set is an enumeration of the source root, not a habit."* It applied that at the **tree** level, inside
> one root. **The root set itself was still a habit.** One root of **22**; **1,753** manifested modules
> of **23,530** raw across the discovered universe. The correction moved the defect up one level; it did
> not remove it.

**Bound on this section, stated so it is not over-read.** 22 roots is the result of **one** declared
pattern (`addons/base/models/res_currency.py`). A core root that omits or relocates that file is **not**
discovered by it. This is a **class `A` bounded enumeration over a declared pattern, not a proof that 22
is the total.**


---

## 3. What changed

| # | Change | Direction |
|---|---|---|
| `Δ1` | v18 point release **added** branch-preferred rate resolution | Narrows resolution to the acting branch |
| `Δ2` | v19 **does not carry `Δ1`** | Reverts to root-scoped resolution |
| `Δ3` | v19 **added** an ORM-core raw-SQL rate resolver on grouped monetary aggregation | Adds an eleventh read path, outside every record rule |

---

## 4. Stable vs unstable

| Element | Across V18-A, V18-B, V19-A, V19-B |
|---|---|
| **Table name and columns** | **STABLE** |
| **Unique constraint** `unique (name, currency_id, company_id)` | **STABLE** |
| `company_id` **nullable** (company-less rows legal) | **STABLE** — and it is the root of `GB-03`'s open axis |
| `_get_rates` domain `('company_id','in',(False, company.root_id.id))` and order `company_id.id, name DESC` | **STABLE** |
| **`_get_conversion_rate` branch preference** | **UNSTABLE** — present in **5 of 22 discovered roots** (§2.4), absent in every v19 root and in the parent round's own research root |
| **ORM-core `sum_currency` resolver** | **UNSTABLE** — present in v19 only |
| **Number of read paths to the rate table** | **UNSTABLE** — v19 adds one in the core |

> **The schema is stable. The semantics are not.** Everything that would appear in a data-model
> comparison matches; everything that determines *which number is produced* does not.

---

## 5. Does migration evidence exist?

> # **NO. And that is the material fact.**

| Question | Answer |
|---|---|
| Does `Δ1` change the schema? | **No.** Identical columns, identical constraint |
| Is there a migration script for `Δ1`? | **No** — a pure behavioural change in a point release produces none |
| Is there an upgrade artefact of any kind for `Δ1`? | **No** |
| Would a migration gate inspecting DDL detect `Δ1` or `Δ2`? | **No.** There is nothing for it to inspect |
| Does `Δ3` change the schema? | **No.** It is a new query against an unchanged table |

**Consequence:** the programme's migration control is DDL-shaped. **These three changes are invisible
to it.** A v18 minor upgrade, or a v18 → v19 move, silently changes which company's rate values a
branch's transactions — and no artefact exists for any reviewer to review.

---

## 6. Downstream accounting consequence

| Area | Consequence |
|---|---|
| **Initial recognition** | The functional-currency amount of a branch's foreign-currency transaction differs between V18-B and v19 whenever branch and root hold different rate rows |
| **Unrealised revaluation** | Period-end revaluation is computed from the same resolver. A silent change of resolver changes the revaluation, hence P&L |
| **Realised FX** | The realised gain or loss is the difference between two conversions. If the two are taken under different resolvers — one before an upgrade, one after — **the realised amount is an artefact of the upgrade, not of the market** |
| **Comparatives and restatement** | Prior-period figures re-derived after an upgrade will not reproduce the figures originally reported. **There is no journal entry recording why** |
| **Consolidation** | Root-scoped resolution is what makes consolidation coherent; branch-preferred resolution is what makes branch-level reporting coherent. **V18-B and v19 choose differently, and the programme spans both** |
| **On-screen aggregates (`Δ3`)** | Any multi-currency grouped total in list, pivot or graph is converted **at today's rate**, not at transaction dates, **outside every record rule**, with a **silent par fallback**. A number that looks like a ledger total is not one |

---

## 7. SaaS / tenant / company consequence

1. **The branch axis is the tenant axis.** SMEsPlus's multi-company model is where `Δ1`/`Δ2` bite. The
   question *"does a branch use its own rates or its root's?"* is a **tenant-semantics** question that
   the reference implementation answers **differently in different releases**.
2. **`Δ3` bypasses record rules**, so the query's scoping is `company_id IS NULL OR company_id = root_id`
   **regardless of which companies the user may read**. It is a rate-table read, not a ledger read — but
   it is the input to a displayed monetary total.
3. **Company-less rows are legal in every version.** In a shared database they are **cross-tenant by
   construction**: one tenant's company-less row is a candidate rate for every other tenant. This is
   `GB-03`'s open axis and it is **stable across all four trees** — the one thing that does not vary.
4. **A single-tenant reading of any of this is unsafe.** The behaviour differences are invisible in a
   one-company database and material in a many-company one.

---

## 8. Wave B dependency

| Wave B element | Dependency on `GB-08` |
|---|---|
| Foreign-currency **customer invoice** recognition | **HARD.** The invoice's functional amount is the resolver's output |
| **Payment** at a different rate, and realised FX on settlement | **HARD.** Two resolver calls; the difference is the P&L |
| **Credit notes** and reversals in foreign currency | **HARD.** Must reproduce the original resolution or the reversal will not net to zero |
| **Aged AR** in presentation currency | **HARD**, and it is `Δ3`'s home: aged-AR views are grouped monetary aggregations |
| **AR reconciliation** across currencies | **HARD** |
| Domestic-only AR | **NONE** |

> **Wave B cannot define AR revenue measurement in foreign currency without knowing which resolution
> semantic SMEsPlus is building to.** This is the single largest Wave A → Wave B carry-forward.

---

## 9. Architectural risk if prematurely frozen

| If frozen to… | Risk |
|---|---|
| **V18-B behaviour** (branch-preferred) | Freezes to a semantic that **the reference implementation itself abandoned in v19**. Every future v19 uplift diverges permanently, and the divergence is invisible to a DDL migration gate |
| **v19 behaviour** (root-scoped) | Freezes to a semantic that **cannot express a branch with its own rates** — a real requirement in multi-branch Thai entities. And it inherits `Δ3`, whose behaviour (`today`'s rate, no record rule, par fallback) is a **defect**, not a design |
| **Either, without deciding the company-less row** | Freezes the *branch* axis while leaving `GB-03`'s **null** axis open. The null axis is the wider defect and has a **database-level route to it** (deleting a company converts its rate rows into company-less rows by foreign key, with no ORM call and no revalidation) |
| **Any freeze, now** | The choice is being made under a **non-converged method** (`MC-01`…`MC-10`: 8 not met, 2 partially met, 0 met) and with **12 tolerance-zero boundaries unresolved**. Freezing an architecture on a research base that its own convergence test rejects is the risk the Gate exists to prevent |

---

## 10. Options — evidence-supported, unranked, for Boss selection

> **No option is recommended and none is selected here.** Each is stated with what the evidence does
> and does not support.

### Option A — `FREEZE CURRENT VERIFIED SEMANTIC`
Freeze to one named tree's behaviour, cited by file and line.
**Supported by:** the semantics are now pinned to a three-line diff and a named SQL block; there is no
ambiguity about *what* would be frozen.
**Not supported by:** the evidence gives no ground to prefer V18-B's answer over v19's — the reference
implementation asserts both. A freeze here selects between two vendor positions, not between a right
and a wrong one.

### Option B — `FREEZE INTERFACE ONLY / DEFER IMPLEMENTATION DETAIL`
Freeze the *contract* — "a rate resolution takes (currency, company, date) and returns a rate or an
explicit failure" — and defer which company the resolver walks to.
**Supported by:** the **schema is stable across all four trees**, so an interface freeze rests on the
part of the evidence that does not vary. It unblocks Wave B's data contracts without deciding the
disputed semantic.
**Not supported by:** it does not answer the AR foreign-currency questions in §8, which need the
resolution rule itself, not only its signature.

### Option C — `HOLD BUILD FREEZE PENDING ADDITIONAL EVIDENCE`
**Supported by:** two evidence gaps are cheap and open. **(i)** No executed test exists — every
statement here is source-derived; a running-instance test on a root + branch with divergent rate rows
would settle actual behaviour in hours. **(ii)** The target build is not declared: the programme spans
four trees and **has not stated which one SMEsPlus ships**.
**Not supported by:** it leaves Wave B's foreign-currency AR scope open, and §8 shows that is most of
foreign-currency AR.

### Option D — `REJECT REFERENCE-SPECIFIC BEHAVIOR / DEFINE SMEPLUS CLEAN-ROOM SEMANTIC`
Define SMEsPlus's own rule from accounting first principles — for example: *a rate row must name
exactly one company; a company-less row is illegal; resolution walks the company hierarchy in a single
declared direction; a missing rate is an error, never par.*
**Supported by:** this is the **only** option that addresses the defects rather than choosing between
them. All four verified pathologies — the company-less row, the par fallback, `today`-dated conversion,
and record-rule bypass — are **properties of the reference implementation, not requirements of
accounting**. It is also consistent with the clean-room rule that reference behaviour is evidence, not
authority.
**Not supported by:** it is the largest amount of work, it forfeits reference-implementation
compatibility on a core path, and it must still answer `GB-03`'s null axis before it can be specified.

---

## 11. What is *not* a Boss decision

These are research or engineering items and must not be routed into `GB-08` to make it look decidable:

| Item | Owner |
|---|---|
| Which build SMEsPlus actually ships | **Programme declaration** — a fact to be stated, not a decision |
| An executed test on a running root + branch instance | **Research** — `MCU-01`, open |
| `Δ3`'s `today`-dated conversion, par fallback and rule bypass | **Verified defects** (`MCU-20` / `BW-31`), not options |
| `GB-03`'s null axis | **Open verified defect** with a database-level route; it is `GB-03`, not `GB-08` |

---

> # `BOSS DECISION REQUIRED — GB-08`
>
> **The decision is: which rate-resolution semantic does SMEsPlus build to, and against which reference
> build is it frozen — if any.**
>
> A genuine Boss-only decision remains. Nothing in this file selects it.
