# ACCOUNT WAVE A — `GB-08` EVIDENCE TRACE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Date `2026-09-04`

> **Every row below was re-derived from primary source in this session.** Nothing is inherited from the
> parent package. Where this session reproduces a parent result exactly, it says so; where it
> **corrects** one, it says that too and names the correction.
>
> Re-runnable: `VOL=/Volumes/iMacSys bash LAYER2_GB08_EVIDENCE/gb08_evidence.sh`
> Captured output: `LAYER2_GB08_EVIDENCE/gb08_evidence_output.txt`

---

## 0. Declared search basis — stated before any result is used

Per `smeplus-denominator-completeness-rule`, a count is only usable if all four are declared and none is
author-chosen:

| Element | Declaration |
|---|---|
| **POPULATION** | Every reference core root reachable on the evidence volume |
| **PATTERN** | The literal path suffix `addons/base/models/res_currency.py` |
| **PATH SET** | Whatever that pattern returns under `/Volumes/iMacSys`, unfiltered and unranked |
| **UNIT** | One directory containing that file = one "reference core root" |

**What this basis cannot see, stated up front:** a core root that omits or relocates
`addons/base/models/res_currency.py`; anything outside `/Volumes/iMacSys`; a running instance. This is a
**class `A` bounded enumeration over a declared pattern**, not a proof of totality.

---

## 1. `E-01` — the root set

```
find /Volumes/iMacSys -type f -path "*/addons/base/models/res_currency.py"
```

**22 roots.** Reproduces the parent's `FC-F4` count **exactly**.

## 2. `E-02` — the 22 roots are **not disjoint** · `GB08-F3` **NEW**

Mechanical prefix test over the root set returns three containment relations:

```
./ODOO/ODOO-COMMUNITY/Odoo18/t8master            CONTAINS  .../t8master/smeplus-server
./ODOO/ODOO-COMMUNITY/Odoo18/t8master            CONTAINS  .../t8master/smeplus-server/odoo
./ODOO/ODOO-COMMUNITY/Odoo18/t8master            CONTAINS  .../t8master/smeplus-server/odoo_old
./ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server  CONTAINS  .../smeplus-server/odoo
./ODOO/ODOO-COMMUNITY/Odoo18/t8master/smeplus-server  CONTAINS  .../smeplus-server/odoo_old
```

**19 disjoint roots, not 22.** `t8master` (2,636 manifested modules) *contains* `smeplus-server`
(1,304), which *contains* `odoo` (637) and `odoo_old` (28).

> ### `GB08-F3` — the "1,753 of 23,530" fraction has an overlapping denominator.
> Summing manifested modules over 22 roots **double-counts the nested chain**. The arithmetic is
> reproduced exactly (`1,753` for the parent's root; `23,530` as the naive sum), but `23,530` is **not a
> count of distinct modules** — the disjoint sum is `23,530 − 1,304 − 637 − 28 = 21,561` over 19 roots.
> **The parent's `FC-F4` correctly identified that the root set was undeclared. It then published a
> fraction whose denominator has the same defect one level down: `PATTERN` and `PATH SET` were declared,
> `UNIT` was not tested for disjointness.**

## 3. `E-04` — 22 roots carry only **4 distinct** `res_currency.py` contents · `GB08-F2` **NEW**

SHA-256 of `addons/base/models/res_currency.py`, per root:

| Digest (first 12) | Roots | `Δ1` | Line | Reading |
|---|---|---|---|---|
| `277f428f0566` | **5** | **PRESENT** | v18 late | `18.0.1`, `18.0.2_community_enterprise`, **`18.0.3_smeplus`**, `MIGRATION/…/odoo-18.0.post20260605`, `ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605` |
| `784a62e190a7` | **7** | ABSENT | v18 earlier | includes **`SMEsPlus18/odoo-18.0+e.20250608`** — the root Wave A researched |
| `09af473416f6` | **9** | ABSENT | v19 | every v19 tree |
| `5f241365cb9a` | **1** | ABSENT | v18 legacy | `t8master/smeplus-server/odoo_old` |

> ### `GB08-F2` — "5 of 22" counts **copies**, not behaviours.
> The behavioural denominator is **4 distinct file contents**, of which **1** carries `Δ1`. Five roots
> hold **the same bytes**. Copies are not independent evidence, and "5 of 22" reads as breadth of
> adoption when it is in fact **one variant, duplicated five times**.

## 4. `E-05` — `Δ1` tested twice, structurally and by string

The parent's test was the exact comment string `Get rates through branch if selected company`. A
comment is not load-bearing, so this session added an independent **structural** test: does the body of
`_get_conversion_rate` reference `root_id`?

**The two tests agree on all 22 roots** — same 5 PRESENT, same 17 ABSENT. The string test is therefore
sound here, and the parent's result is **reproduced exactly**.

## 5. `E-06` / `E-07` — which root Wave A actually researched

| Root | Digest | `Δ1` |
|---|---|---|
| `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo` — **Wave A's declared research root** | `784a62e1` | **ABSENT** |
| `CLAUDE AI/MIGRATION/ODOO18/18.0.3_smeplus/odoo` — **the only root whose name asserts the SMEsPlus line** | `277f428f` | **PRESENT** |

Reproduces the parent's `FC-F2` exactly.

## 6. `E-21` — the **complete** v18 divergence is the `Δ1` hunk and nothing else

```
diff -u  SMEsPlus18/odoo-18.0+e.20250608/…/res_currency.py \
         MIGRATION/ODOO18/18.0.3_smeplus/…/res_currency.py
```

returns **one hunk, seven lines**:

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

**Nothing else in the file differs.** This bounds the v18 question completely: whatever `Δ1` does or does
not do is the whole of the v18 divergence in `res_currency.py`.

---

## 7. `GB08-F1` — **`Δ1` does not change which rate row is selected.** NEW · CORRECTS THE PARENT

This is the single most consequential result in this document, so it is stated as a derivation with
every premise named and separately verified.

**Premise 1 — the call chain.** `_get_conversion_rate` does not read rates. It passes `company` into
`with_company(company)`, which sets `self.env.company`, and then reads `.inverse_rate`:

```python
return from_currency.with_company(company).with_context(to_currency=…, date=…).inverse_rate
```
`base/models/res_currency.py:271` (`18.0.3_smeplus`)

**Premise 2 — what actually reads the rate rows.** `_compute_current_rate` calls
`(self + to_currency)._get_rates(self.env.company, date)` — `base/models/res_currency.py:155`.

**Premise 3 — the only use `_get_rates` makes of that company.**
`base/models/res_currency.py:121–163`, full body read:

```python
rate_query = self.env['res.currency.rate']._search([
    ('name', '<=', date),
    ('company_id', 'in', (False, company.root_id.id)),
    ('currency_id', '=', currency_id),
], order='company_id.id, name DESC', limit=1)
```

The company appears **once**, as `company.root_id.id`.

**Premise 4 — `root_id` is the topmost ancestor.** `base/models/res_company.py:115–118`:

```python
company.parent_ids = self.browse(int(id) for id in company.parent_path.split('/') if id) if company.parent_path else company
company.root_id = company.parent_ids[0]
```

Therefore for every company `C` in a tree rooted at `R`: `C.root_id == R`, and in particular
`branch.root_id == root.root_id == R`.

**Premise 5 — neither method is overridden anywhere.** Searched **all 22 roots** for
`def _get_rates(self, company, date)` and `def _get_conversion_rate(self, from_currency, …)`: each is
defined **exactly once per root**, in `addons/base/models/res_currency.py`. Every other `_get_rates` /
`_get_conversion_rate` in the volume is a **different method on a different model** with a different
signature (`delivery_dhl_rest`, `delivery_usps_rest`, `l10n_ch_hr_payroll`, and the no-argument
`l10n_ar_withholding` wizard).

**The derivation.** `Δ1` substitutes `self.env.company` (a branch) for a passed value equal to
`self.env.company.root_id`. Enumerating every case:

| `env.company` | caller passes | with `Δ1` → company | without `Δ1` → company | `company.root_id` |
|---|---|---|---|---|
| branch `B` of root `R` | `R` | `B` | `R` | **`R` either way** |
| branch `B` of root `R` | `None` | `B` | `B` | `R` |
| branch `B` of root `R` | `B` | `B` | `B` | `R` |
| branch `B` of root `R` | `X` (other tree) | `X` | `X` | `X.root_id` |
| root `R` | `R` | `R` | `R` | `R` |
| root `R` | `None` | `R` | `R` | `R` |

> **In every case the search domain is identical.** `Δ1` changes *which company object is carried*, and
> `_get_rates` then collapses it back to the same root. **The rate row selected is unchanged.**

**Premise 6 — the one remaining company-dependent input, closed.** `_compute_current_rate` also does
`to_currency = browse(ctx to_currency) or company.currency_id`. Two independent reasons this cannot
differ: (i) `_get_conversion_rate` always supplies `to_currency` in the context, so the fallback is not
reached on this path; (ii) a branch's currency is **constrained equal to its root's** —
`res_company.py:95–103` `_get_company_root_delegated_field_names() → ['currency_id']` and
`res_company.py:422–429` `_check_root_delegated_fields` raises `ValidationError` otherwise. **Verified
present and identical in all four variants.**

### Bounds on `GB08-F1` — stated so it is not over-read

| Bound | Status |
|---|---|
| It is a **static derivation over source**, not an executed test | **`MCU-01` remains open and is now more valuable, not less** |
| It covers the resolver chain reachable from `_get_conversion_rate` | **Verified** — no overrides in 22 roots |
| It assumes `parent_path` is populated | Odoo's own invariant; a company with an empty `parent_path` computes `root_id = itself` (`res_company.py:117`) — an edge case not separately tested |
| It says nothing about custom SMEsPlus modules outside the 22 roots | **Out of the declared path set** |
| It does **not** say `Δ1` is harmless | It changes the ORM compute **cache key** (`@api.depends_context('company')`) and it *reads* as a branch-preference feature to any engineer who meets it |

> ### `GB08-C1` — the parent's characterisation is corrected.
> Parent `GB-08` §3 recorded `Δ1` as *"Narrows resolution to the acting branch"*, and §6 as *"The
> functional-currency amount of a branch's foreign-currency transaction differs between V18-B and
> v19."* **Neither is supported by the code.** The v18 and v19 `_get_conversion_rate` bodies are, apart
> from the inert `Δ1` hunk, **byte-identical**, and `_get_rates` is semantically identical in both.
> **There is no v18-vs-v19 branch-rate divergence to decide between.**

---

## 8. `E-10` / `E-11` — `Δ3` is real, and it is the only live version divergence

`orm/models.py`, `_read_group_select`, branch `func == 'sum_currency'`
(`SMEsPlus19/odoo-19.0+e.20260312/odoo/orm/models.py:1972–2003`), verified verbatim this session:

```sql
(SELECT DISTINCT ON (currency_id) currency_id, rate
   FROM "res_currency_rate"
  WHERE company_id IS NULL OR company_id = <env.company.root_id.id>
  ORDER BY currency_id,
           company_id,
           CASE WHEN name <= <Date.context_today> THEN name END DESC,
           CASE WHEN name >  <Date.context_today> THEN name END ASC)
```
joined `LEFT JOIN` and consumed as `SUM(amount / COALESCE(rate, 1.0))`.

**Occurrence count, all 22 roots:** `sum_currency` appears in **0 files in every one of the 13 v18
roots** and in **8–12 files in every one of the 9 v19 roots**. Reproduces the parent's `Δ3` exactly.

> ### `GB08-F9` — `Δ3` is not merely "rule-bypassing". Its scope is **different**. NEW
> The record rule (§9) admits `company_id parent_of company_ids` — the ancestors of **every** company
> the user may act in. `Δ3` hardcodes `env.company.root_id` alone. `Δ3` therefore also **ignores the
> user's allowed-company set**, which is a narrowing, not only an absence of a check.

> ### `GB08-F11` — three models opt **out** of `Δ3` server-side. `account.move.line` does not. NEW
> `budget.line` (`account_budget/models/budget_line.py:95–126`), `analytic.account`
> (`analytic/models/analytic_account.py:128–160`) and `stock.quant`
> (`stock_account/models/stock_quant.py:67–77`) override `_read_group_select` to intercept
> `…:sum_currency` and compute in **Python** via `currency_id._convert(...)` instead. Searched
> `account/models/account_move_line.py` for `_read_group_select` / `_read_group_postprocess_aggregate`:
> **no override.** The two accounting overrides that do exist —
> `account_accountant/models/account_move.py:1033` (`sum_rounded`) and
> `account/report/account_invoice_report.py:160` (`price_average:avg`) — delegate everything else to
> `super()` and are **not** opt-outs.
>
> **Reading:** the reference implementation's own authors route three aggregate surfaces around this
> resolver. The **ledger line model is not one of them.**

---

## 9. `E-14` / `E-15` — the record rule and the ACL · `GB08-F8` **NEW**

`addons/base/security/base_security.xml:62–66` — **identical in v18 and v19**:

```xml
<record id="res_currency_rate_rule" model="ir.rule">
    <field name="name">multi-company currency rate rule</field>
    <field name="model_id" ref="model_res_currency_rate"/>
    <field name="domain_force">['|', ('company_id', 'parent_of', company_ids), ('company_id', '=', False)]</field>
</record>
```

No `groups`, no `perm_*` → a **global** rule applying to read, write, create and unlink.

ACL, identical in v18 and v19:

| Group | File | `r,w,c,u` |
|---|---|---|
| `base.group_public` / `group_portal` / `group_user` | `base/security/ir.model.access.csv` | `1,0,0,0` |
| `base.group_system` | `base/security/ir.model.access.csv` | `1,1,1,1` |
| **`account.group_account_manager`** | **`account/security/ir.model.access.csv:7`** | **`1,1,1,1`** |

And the field is editable in the UI: `base/views/res_currency_views.xml:20,44,169` render
`<field name="company_id" groups="base.group_multi_company"/>`.

> ### `GB08-F8` — a cross-tenant write→read path, stable in every version.
> `res_currency_rate.company_id` is **nullable** (`fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.root_id)` — **no `required=True`**, verified in all four
> variants). The global rule **explicitly admits `company_id = False` to every user**. An
> `account.group_account_manager` in **any** company has `create` on the model and an editable
> `company_id`. **Therefore one tenant's accounting manager can create a company-less rate row that
> every other tenant in the same database will read and value transactions with.** This is `GB-03`'s
> null axis, verified here at the rule and ACL level rather than inferred.
>
> The parent stated *"No record rule is applied to `res.currency.rate`"* (§2.2 property 1). **Corrected
> (`GB08-C3`): a rule exists and is stable; it is `Δ3` that does not apply it.** The distinction
> matters, because it means the null-row exposure is present **with or without `Δ3`**.

---

## 10. `E-12` / `E-13` — the fallback chain · `GB08-F4`, `GB08-F5`, `GB08-F6` **NEW**

`_get_rates` in **every one of the four variants** ends:

```python
SQL("COALESCE((%s), (%s), 1.0)", rate_query.select(rate), rate_fallback.select(rate))
```

with `rate_query` = `name <= date`, `order='company_id.id, name DESC'`, `limit=1` and
`rate_fallback` = no date bound, `order='company_id.id, name ASC'`, `limit=1`.

> ### `GB08-F5` — the fallback is **three-tier**, and tier 2 is a **future** rate.
> 1. latest rate with `name <= date`; failing that
> 2. **the earliest rate that exists at all** — with no upper date bound this is, for a transaction
>    predating the rate table, **a rate from the future**; failing that
> 3. **`1.0` — par.**
>
> **The reference implementation never raises on a missing rate.** The same three-tier shape is
> re-implemented inside `Δ3`'s `ORDER BY … CASE WHEN name <= today … DESC, CASE WHEN name > today …
> ASC` plus `COALESCE(rate, 1.0)`.

> ### `GB08-F4` — the silent par fallback is **not new in v19**, and it is **not on the unstable axis**.
> Parent `GB-08` §4 lists the par fallback as a property of `Δ3` (UNSTABLE) and §9 offers *"freeze to
> v18"* as a way to avoid `Δ3`. **`COALESCE(…, 1.0)` is in `_get_rates` in all four variants,
> including both v18 variants.** The oldest variant (`odoo_old`, `5f241365`) is stronger still: its
> `_get_rates` is **raw SQL with `COALESCE(…, 1.0)` and no `_search`**, i.e. **no record rule on the
> primary path** — the very pathology the parent presents as `Δ3`'s novelty.
>
> **`GB08-C2` / `GB08-C5`: the par fallback belongs on the STABLE axis. No version choice removes it.**

> ### `GB08-F6` — precedence is **ownership first, recency second**.
> `order='company_id.id, name DESC'` with PostgreSQL's `NULLS LAST` on ascending order puts
> **company-owned rows before company-less rows**, and only then applies the date. **A stale
> company-specific rate therefore beats a current company-less rate.** `Δ3`'s
> `ORDER BY currency_id, company_id, …` makes the same choice. This is **stable across all four
> variants and both resolvers** — and it is the one precedence rule the reference implementation
> actually commits to.

---

## 11. `GB08-F7` — branch-scoped rate rows are **write-visible dead data**. NEW

Composing §9 and `GB08-F1`:

| Step | Verified at |
|---|---|
| A rate row **may** name a branch — `company_id` is nullable, editable, and defaults to the root but is not constrained to it | `res_currency.py` field def; `res_currency_views.xml:20,44,169` |
| The record rule **shows** such a row to a user of that branch — `('company_id','parent_of',company_ids)` matches the branch itself | `base_security.xml:64` |
| An `account.group_account_manager` may **create** it | `account/security/ir.model.access.csv:7` |
| `_get_rates` will **never select** it — the domain is `(False, company.root_id.id)`, and a branch id is neither | `res_currency.py:130,134` |
| `Δ3` will never select it either — `company_id IS NULL OR company_id = root_id` | `orm/models.py:1980` |

> **A branch-scoped exchange rate can be entered, saved, displayed and reported on, and will never value
> anything.** Stable in all four variants. **This — not the v18/v19 question — is the concrete defect
> under `GB-08`.**

---

## 12. `GB08-F10` — directory naming is not a version indicator. NEW

`./CLAUDE AI/MIGRATION/ODOO18/enterprise` is filed under an **`ODOO18`** path. Its
`addons/base/models/res_currency.py` digest is `09af473416f6` — **the v19 content** — and it carries
**11 files containing `sum_currency`**, which exists in **no** v18 root.

> **It is a v19 tree in an ODOO18 directory.** Any programme control that identifies a build from its
> path is unsound. This directly conditions the "which build does SMEsPlus ship" declaration that
> `GB-08` Option `C` rests on.

---

## 13. Reproduction status of every parent `GB-08` claim

| Parent claim | This session |
|---|---|
| 22 reference core roots | **Reproduced exactly** |
| `Δ1` present in 5 of 22 roots | **Reproduced exactly**, and re-tested structurally — but see `GB08-F2` (5 copies, 1 variant) |
| Wave A's research root has `Δ1` ABSENT; `18.0.3_smeplus` has it PRESENT | **Reproduced exactly** |
| `Δ2` — no v19 root carries `Δ1` | **Reproduced exactly** |
| `Δ3` — v19 ORM-core `sum_currency` resolver, raw SQL, `today`, par fallback | **Reproduced exactly**, and widened by `GB08-F9`, `GB08-F11` |
| `sum_currency` absent from all of v18 | **Reproduced exactly** — 0 files in all 13 v18 roots |
| Schema stable: `unique (name,currency_id,company_id)`, `company_id` nullable, `_get_rates` domain and order | **Reproduced exactly** in all four variants |
| `Δ1` "narrows resolution to the acting branch" | **CORRECTED — `GB08-C1`.** It does not |
| Functional amounts "differ between V18-B and v19" | **CORRECTED — `GB08-C4`.** Not on the verified path |
| Par fallback is a `Δ3` (v19) property | **CORRECTED — `GB08-C2`.** It is in every variant |
| "Freeze to v18" avoids `Δ3`'s par fallback | **CORRECTED — `GB08-C5`.** It does not |
| "No record rule is applied to `res.currency.rate`" | **CORRECTED — `GB08-C3`.** A rule exists; `Δ3` does not apply it |
| "1 of 22 roots · 1,753 of 23,530 modules" | **Arithmetic reproduced; denominator corrected — `GB08-C6`** (§2) |

**Six parent claims reproduced exactly. Six corrected. Zero found unverifiable.**

---

## 14. What remains **not** evidenced

| Gap | Class | Consequence |
|---|---|---|
| **No executed test on a running root+branch instance** | `MCU-01`, open | Every statement here is source-derived. `GB08-F1` in particular is a derivation |
| **The build SMEsPlus ships is still undeclared** | Programme declaration, not research | `GB08-F10` shows path names cannot substitute for it |
| **Custom SMEsPlus modules outside the 22 roots** | Class `A` bounded | An override of `_get_rates` in a module outside the declared path set would invalidate `GB08-F1` premise 5 |
| **PostgreSQL `NULLS LAST` behaviour in `GB08-F6`** | Derived from SQL semantics, not executed | Directionally certain; not measured |
| **Whether any live database holds branch-scoped rate rows** | Not measurable from source | Determines whether `GB08-F7` is latent or active |
