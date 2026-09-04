# MCC_E01 — CONTRADICTIONS TO `MCC_E00` AND TO THIS ROUND, FOUND BY FIXED-POINT PASSES 2 AND 3 (LAYER 2)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Vendor tokens and `file:line` citations.
> **`DR-NC-06` lineage rule applies: `MCC_E00` is NOT edited. This file governs where they conflict.**
> Every reviewer claim recorded below was **re-verified against primary source by this session before
> acceptance.** The verification result, not the reviewer's assertion, is what is recorded.
> `Independent Review ≠ Truth. Verified Evidence = Truth Basis.`

Two fresh reviewers, neither an author of this package nor of any prior round, on disjoint
assignments: `MCCR-A` source-layer re-enumeration (Pass 2); `MCCR-B` adversarial delta search (Pass 3).

---

## 1. THIS ROUND'S OWN CLAIMS, CONTRADICTED AND CORRECTED

### `MCCX-01` — `MCC-E-007` is INVALID. The shipped demo rate rows are NOT null-company.

**Claim contradicted (this round's own):** *"`base/data/res_currency_rate_demo.xml` — 162 records,
`company_id` present: **0 — every row is NULL-company**"*, and the derived finding `MCC-D-04` /
`BW-30` that a demo-seeded database carries 162 company-less rows.

**Raised by `MCCR-A`. Re-verified at source by this session:**

`odoo/models.py:5080` `_prepare_create_values` →
```python
for vals in vals_list:
    # add default values
    vals = self._add_missing_default_values(vals)
```
Data records load through `_load_records` → `create`, and `create` merges field defaults for every
field absent from the values. `res.currency.rate.company_id` carries
`default=lambda self: self.env.company.root_id` (`base/models/res_currency.py:365-366`).

> **The 162 demo rows therefore load with `company_id = <root of the company active at install>`.
> They are ROOT-company rows, not NULL-company rows.**

**Consequences, stated precisely because the correction is partial:**

| Claim | Status after correction |
|---|---|
| "A demo-seeded database ships 162 **null-company** rate rows" | **WITHDRAWN — FALSE.** The XML omits the field; the ORM supplies the default |
| "`MCU-07` CLOSED: no `data` file in either tree ships a rate row" | **STANDS** — independently reproduced by `MCCR-A` across four version trees. `demo` only, in every tree |
| "Null-company rows are reachable out of the box" | **CORRECTED: they are not SHIPPED; they are USER-CREATABLE.** The field is not required, the constraint passes an empty company, the record rule admits `company_id = False` by explicit disjunct, and the field is editable in the shipped list and form views under the multi-company group |
| **`BW-30` — the 2010-dated silent historical fallback** | **STANDS, ON A CORRECTED MECHANISM.** 157 of the 162 rows are dated `2010-01-01`. They belong to the installing root. Any company **inside that root's tree** with no newer rate for a currency resolves every foreign-currency posting at the **2010** rate — silently. A **second root company** in the same database sees none of them and resolves at **par**. Two different wrong answers from one seeding, neither announced |

**Cause of this round's error.** The enumeration read the **data file** and counted the absence of an
element. It did not read the **model default** that the loader applies. **A field absent from a data
file is not a field absent from the row.** This is the same defect class as every other in the
programme — a proxy for the source (the XML) substituted for the source (the loaded record) —
committed by the round that was documenting it, in the file that documents it.

---

### `MCCX-02` — `MCC-E-009` is INVALID. The rate model is NOT stable across the v18 line.

**Claim contradicted (this round's own):** *"the rate-table company-scoping model is STABLE across
the v18 and v19 lines, in every element tested."*

**Raised by `MCCR-A`. Re-verified at source by this session, verbatim:**

`v18 post-20260605 · base/models/res_currency.py:266-274`:
```python
def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
    if from_currency == to_currency:
        return 1
    if company == self.env.company.root_id:
        company = self.env.company  # Get rates through branch if selected company
    else:
        company = company or self.env.company
```

`v18 e-20250608` (`SRC-A`, the SMEsPlus reference build) `:266-271` and **both v19 trees** `:273-278`
carry the plain form with **no branch clause**.

> **`VERIFIED DEFECT — CROSS-VERSION INSTABILITY.` A branch-preference behaviour exists in a LATER
> v18 point release and is ABSENT from v19. Version order does not predict behaviour.**
>
> Under the divergent build, a caller that passes the **root explicitly** has it silently replaced by
> the **active** company — which may be a branch — before scoping. That is the **opposite** direction
> from every other site in the file, and it is the only place in any tree where a branch is preferred.

**Cause of this round's error.** The cross-version comparison was run over a **token list** —
constraint present, resolver filter present, default present, uniqueness present — not over the
**file**. Every token matched, so the files were declared equivalent. **A comparison bounded by a
token list is not a comparison.** Same defect class, third instance in this round, this time in the
version dimension.

**Programme significance.** This reproduces, in the FX domain, the headline finding already recorded
for the costing domain: *the reference ERP's own pattern is unstable across its own versions*. It is
the second independent confirmation of that property and it is now a cross-domain result.

---

### `MCCX-03` — `MCC_E00 §MCC-E-000` understates the unsearched tree, and `MCC_E` mis-states one recount.

| Sub-claim | This round said | Verified | Correction |
|---|---|---|---|
| Archive tree size | "961 directories" | **961 directories · 959 with a manifest** | directory count right; **manifest count is the meaningful figure** |
| Modules outside the primary tree | 961 | **962 manifested modules** = 959 archive + **3 module directories sitting DIRECTLY under the source root** (`stock_fleet`, `stock_fleet_enterprise`, `stock_intrastat`) | **this round missed the 3 stray modules entirely.** Raised by `MCCR-B`, reproduced here: `find <root> -name '__manifest__.py' -not -path '*/addons/*' \| wc -l` → **962** |
| Localisation surface | not stated | **`addons/` holds 2 `l10n_*` modules; `addons_archive/` holds 904** | raised by `MCCR-A`. **Every localisation claim in the programme's history is bounded to a tree containing 2 of 906 localisations** |
| Elevation-site recount | this round reported **94**, "reproduces the correction" | **93 under the declared pattern**; 94 only under a looser pattern that also matches the single de-elevation call | **`MCC_E` §2 is CORRECTED to 93.** `MCE02`'s `MCX-06` correction of 93→94 is itself **NOT PROVEN**: the parent's declared pattern excludes de-elevation by construction and returns 93 on re-execution. **The original `MCE00` figure was right and the correction was wrong** |
| Wave A model count `P-13` | inherited as 21 | **22** distinct model names over the same 18 files | raised by `MCCR-B`, reproduced here. The omitted model creates and links journals and is one of the nine enabling the company-consistency check. **`P-13` is labelled `D-SRC` in the canonical matrix and is in fact author-derived** |

---

## 2. NEW MATERIAL FINDINGS FROM PASS 2 — verified before acceptance

### `MCCX-04` — v19 adds an ELEVENTH read-side rate resolver, in the ORM CORE, bypassing every record rule

**Raised by `MCCR-A`. Re-verified verbatim at `v19 e-20260312 · odoo/orm/models.py:1972-1998`:**

A `sum_currency` aggregator, new in v19 (**zero occurrences in either v18 core**), injects a raw-SQL
sub-select over the rate table into any grouped read:

```sql
SELECT DISTINCT ON (currency_id) currency_id, rate
FROM "res_currency_rate"
WHERE company_id IS NULL OR company_id = <env.company.root_id.id>
ORDER BY currency_id, company_id,
         CASE WHEN name <= <today> THEN name END DESC,
         CASE WHEN name >  <today> THEN name END ASC
```

**Four verified properties, each material:**

1. **Raw SQL joined into the grouped query — no record rule on the rate table applies.**
2. **A FOURTH fallback semantic.** When no rate exists at or before today it takes the **earliest
   FUTURE rate**. The posting resolver takes the earliest rate *ever*; the reporting currency table
   takes **par**; this takes a future rate. Four resolvers, four different answers to "no rate".
3. **It converts at `today`, not at the record's date.** A grouped total of monetary values is
   translated at today's rate regardless of when the facts occurred.
4. **Reachability is broad, not narrow.** Consumers named by the reviewer and consistent with the
   call site include analytic accounts, budget lines, stock valuation, and the generic list/pivot/graph
   aggregation layer — i.e. **any monetary column aggregated in any list or pivot view.**

> **A v18 → v19 migration WIDENS the rate-scoping universe rather than converging it.** This is
> directly material to the SMEsPlus target line and is **`GATING`** for any Wave A conclusion that is
> meant to carry into v19. Registered as `MCU-20`.

### `MCCX-05` — the company-consistency ENFORCEMENT surface, enumerated by no round, contains 16 inert guards

**Raised by `MCCR-B`. Every number re-counted by this session over the 18-file Wave A surface:**

| Sub-population | Verified |
|---|---|
| Models enabling automatic company-consistency checking | **9** of 22 |
| Relational field declarations | **139** |
| … of which opt into the company check | **36** (25.9%) |
| … of which do **not** | **103** |

**The sharpest instance, re-verified independently:** the company model declares **16** relational
fields carrying the company-consistency flag — the destinations of automatically generated ledger
facts including exchange difference, cash difference, suspense, accrual and cash-basis accounts.
**Neither the framework's company model nor the accounting addon's extension of it enables automatic
checking, and the accounting addon contains ZERO explicit invocations of the check.**

> **All 16 declarations are inert. A control that is present to a reader and absent to the machine.**
> The eleven company-domain overrides that `MCE-005` enumerated are the *content* of a check gated by
> two populations nobody counted.

Registered as tolerance-zero candidate **`T0-09` — declared-but-inert control**, alongside the
already-known empty constraint definition on the entry model. Two instances bound the class.

### `MCCX-06` — cross-branch reconciliation: the settlement guard tests the ROOT, not the company

**Raised by `MCCR-B`. Re-verified verbatim at `account/models/account_move_line.py:2336-2340`:**

```python
if len(self.company_id.root_id) > 1:
    raise UserError(_("Entries don't belong to the same company: %s", ...))
```

For journal items in two **branches** of one root, `self.company_id.root_id` is a **single** record,
so `len == 1` and **no error is raised**. The user-facing message and the method's own docstring both
assert company-level enforcement the code does not perform.

**Re-verified corroborating facts:**

- `account/models/account_partial_reconcile.py:14-20` — the two linking fields are plain relations
  carrying **no company-consistency flag**; the model enables **no** automatic checking (`MCCX-05`).
- `account/models/account_partial_reconcile.py:87-94` `_compute_company_id` — assigns the partial to
  the **debit side if it is an invoice, else the credit side**. One of the two companies is chosen;
  the other is silently dropped from the settlement record.
- `account/models/account_move_line.py:2738-2741` — the exchange-difference entry's company is
  `(…).company_id or company)[:1]` — **a two-record recordset truncated to its first element.** The
  FX gain or loss is then booked in an arbitrarily selected legal entity, using that entity's exchange
  journal and accounts, on lines carrying the other entity's accounts.
- The reconciliation models carry **no record rule anywhere in the tree** — the programme's
  longest-standing class-`A` verified absence — and full create/write/unlink rights for ordinary
  accounting roles.
- `account/models/account_full_reconcile.py:52-66` — the resulting link is written onto both
  companies' journal items by **raw SQL**, below the ORM, the record rules and every lock check.

> **`VERIFIED DEFECT` (mechanism) · `NOT PROVEN` (runtime, not executed).**
> A receivable in one branch can be recorded as settled by cash that never entered it; no
> intercompany balance is created; the FX result lands in the wrong entity; and the settlement link
> is written below every control. **Every move balances and every trial balance foots.**
>
> **This is a NEW tolerance-zero-severity class.** It is not the partner-merge case, not the
> account-merge case, and not the rate case. It is reachable by an ordinary accounting user in the
> normal branch configuration.

**Generalisation the reviewer supplied and this session accepts as a class:** the same
root-level-guard-over-branch-level-fact shape recurs at further sites in the payment-register,
bank-statement, tax and partner paths. `P-21c` counts 37 such references and assesses 4.

### `MCCX-07` — the posted-move immutability control is suppressed on the bank path

`account/models/account_move.py:3246-3250` lists the fields unmodifiable on a posted move and exempts
them under a skip flag. The **only production consumers of that flag in the accounting addon** are
four writes to **posted** moves in the bank-statement line model. That flag falls inside `MCE-005`'s
generic bucket of 48 skip tokens — **counted, never assessed**.

The bank-statement line model is in **neither** the 18-file surface **nor** the corrected 26-file
surface. Registered against `T0-03`.

---

## 3. REVIEWER CLAIMS REDUCED OR REJECTED ON VERIFICATION

Recorded because the discipline must be visible in both directions.

| Claim | Outcome |
|---|---|
| `MCCR-A`: "12 distinct scoping rules, 10 read-side" vs this round's "14" | **NEITHER IS WRONG. The UNIT was never defined.** `MCCR-A` counted distinct *expressions* and collapsed six identical raw-SQL predicates into one; this round counted *sites bearing an expression*. Over the same bounded surface, two disciplined enumerations returned 12 and 14. **A bounded population with an undefined unit of count is not yet a denominator.** Recorded as a finding in its own right — `MCC_E` §5, and carried to `MCC_K` |
| `MCCR-A`: the 3 stray module directories are part of "962" | **CONFIRMED**, and it is this round that was short |
| `MCCR-B`: `P-15` tuple count is 9, not 11 | **CONFIRMED** — agrees with `MCX-05`; the registers still publish 11 |
| `MCCR-B`: object-button count 39 or 92, never 55 | **ACCEPTED AS UNRESOLVED.** Already withdrawn at `MCE02`; not re-derived here |
| `MCCR-B`: gating unknowns rise to "at least 20" | **PARTIALLY ACCEPTED.** The two reclassifications are evidenced and accepted; the double-count observation is accepted; the arithmetic is not adopted wholesale because this round independently *closed* 8. Net position is in `MCC_D` §5 and `MCC_H` |
| `MCCR-B`: `MCU-60`/`MCU-61` "out of scope with evidence" is unsupported | **ACCEPTED.** No search pattern or path set for either appears in any file of the parent package. Both revert to class `B`, reclassified `UNKNOWN` |
| `MCCR-A`: the brief's ORM-core path does not exist | **CONFIRMED — and it is this session's error.** The reviewer brief written by this session named a path one directory too deep. The reviewer found the real path and said so. **Had it not, a class-`B` result would have been scored class `A`** — the exact failure the standard exists to prevent, injected by the round conducting the test |
| `MCCR-A`: spreadsheet RPC endpoint is bounded by an access error on unauthorised companies | **ACCEPTED, and it REDUCES this round's own `MCC_E00 §MCC-E-008` characterisation.** The endpoint routes through the active-companies mechanism, which raises rather than silently returning par for a company the user cannot access. The par outcome remains reachable **within** the user's own allowed companies |

---

## 4. Net effect on this round

| Measure | Value |
|---|---|
| This round's own claims **invalidated** by a fresh pass | **3** — `MCC-E-007` (demo rows), `MCC-E-009` (cross-version stability), `MCC_E` §2 (elevation recount) |
| This round's own claims **understated** and corrected upward | **2** — unsearched-tree size, `P-13` |
| This round's own **method errors** recorded against itself | **4** — the XML-vs-loaded-record proxy, the token-list version comparison, the missed stray modules, and a wrong path in its own reviewer brief |
| New material finding classes returned by the fresh passes | **4** — `MCCX-04`, `MCCX-05`, `MCCX-06`, `MCCX-07` |
| New tolerance-zero candidates | **2** — `T0-08` entry identity, `T0-09` declared-but-inert control |
| Reviewer claims reduced or rejected on verification | **3** |
| Vetoes issued | **1 partial** — `MCCR-A` vetoes *any convergence claim resting on the branch-rate constraint alone*. **This session accepts that veto and no such claim is made** |
