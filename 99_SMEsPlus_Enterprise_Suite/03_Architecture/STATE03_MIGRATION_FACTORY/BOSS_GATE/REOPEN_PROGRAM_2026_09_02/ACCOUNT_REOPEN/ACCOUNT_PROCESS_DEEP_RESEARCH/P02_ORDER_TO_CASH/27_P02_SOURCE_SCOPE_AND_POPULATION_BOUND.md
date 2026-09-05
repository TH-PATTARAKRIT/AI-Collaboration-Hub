# 27 — P02: THE SOURCE SCOPE IS NOT THE DEPLOYED CODE

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

Produced after a second peer exchange (P04). **This is the most package-bounding file in P02** and it
should be read before any source-derived negative claim anywhere in the package.

## 1. The Check, And Why It Was Run

P04 reported that against its own deployment, **27 of 361 installed modules were in neither of its declared
source roots**, and warned that *a source scope named by a build string does not identify code*.

P02 ran the same check against `idemo18_uat` — the v18 deployment P04 supplied, and the only deployed
database on the generation P02's entire source analysis was written against.

## 2. Result

**`FACT VERIFIED` — SC-01. Of 361 installed modules, 66 are NOT in P02's declared v18 source root.**

| | |
|---|---|
| Modules installed in the deployment | **361** |
| Present in the declared root | **295** |
| **Absent from the declared root** | **66 (18%)** |

**`FACT VERIFIED` — SC-02. The build string does not identify the code.** Two directories on this host
carry the same build `18.0+e.20250608` and hold **797** and **799** addons respectively. P02 declared one
of them by path and cited it as *the* v18 root throughout.

## 3. The Modules That Matter To P02

Among the 66 absent modules, by name alone:

| Module | Why it bounds a P02 finding |
|---|---|
| **`inherit_sales`** | By name, an override of the sales module — **the module P02 is about**. |
| **`inherit_inventory`** | By name, an override of the inventory module — the other module P02 is about. |
| `account_invoice_fixed_discount` | Directly concerns `11` §7a, P02's discount analysis. |
| `account_payment_multi_deduction` | Directly concerns `09`, P02's settlement analysis. |
| **`l10n_th_withholding_tax`** | See §4. |
| **`l10n_th_withholding_tax_cert`** | See §4. |
| **`l10n_th_withholding_tax_cert_form`** | See §4. |
| **`l10n_th_withholding_tax_report`** | See §4. |
| `om_data_remove` | The module a peer process recorded as its **highest-severity finding**. |
| `full_summarize_bills`, `journal_entries_report`, `print_voucher_request` | Accounting-document behaviour, unexamined. |

**`FACT VERIFIED` — SC-03. `inherit_sales` and `inherit_inventory` are installed in the deployment and
exist NOWHERE on this host.** The code that modifies sales and inventory behaviour in the only deployed
v18 system **cannot be read at all**.

## 4. C-32 — A Published `VERIFIED ABSENCE` Is Refuted

`L2_AUDIT_QUARANTINE/T3` §5 and §10 published, as **`VERIFIED ABSENCE` within the population**:

> *"No withholding certificate model … not found in the entire addons root (791 module dirs, all file
> types, recursive) under the patterns `is_withholding`, `withholding_sequence`"*, and
> *"no module directory matches `*withhold*` or `*wht*`."*

**Refuted.** The deployment has **four** Thai withholding modules installed —
`l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_cert_form`,
`l10n_th_withholding_tax_report` — and **all four exist on this host, in three copies each**, in
directories entirely outside the declared root.

**The negative was true within its stated boundary and false in use** — precisely the failure P04
described in its own census. The boundary was declared honestly; **the boundary was the wrong one**, and
nothing in the claim signalled that the root it named was not the code the system runs.

**Consequence for the Thai track:** `06` §3's *"Withholding-tax accrual or certificate event on a customer
receipt — `VERIFIED ABSENCE`"* is **withdrawn**. P02 cannot say whether customer-side withholding is
handled, because the modules that would handle it were never read. **Routed to P07**, which owns Thai tax
and has independently recorded findings about these same modules.

## 5. What This Bounds

**Every source-derived negative claim in this package is scoped to a code base that omits 18% of the
deployed modules, including two that by name override the two modules P02 is about.**

That does **not** invalidate the mechanism analysis — reading how the standard product works is exactly
what clean-room benchmark learning requires, and the mechanisms are correctly read. It **does** mean:

| Claim class | Status |
|---|---|
| *"The standard product does X"* | **stands** — correctly read from the standard product |
| *"No mechanism for Y exists"* | **bounded, and one is already refuted** (§4) |
| *"The deployment behaves as X"* | **not supported** — 66 modules unread, 2 unreadable |

**`FACT VERIFIED` — SC-04.** P02's declared path set has now failed on **three axes**: the archive path
set (`RE-20`), the runtime path set (`RE-21`), and now the **source** path set. In every case
POPULATION, PATTERN and UNIT were declared and executed, and the **path set was chosen and not
validated against what the system actually runs**.

## 6. RE-22 — A Sixth Evidence-Base Failure: Publishing A Partial As A Total

`26` §9 published *"16 database-bearing artefacts … 7 distinct databases"*.

**That was a read of a background job that was still running.** On completion it stood at **26 artefacts
and climbing**, including an entire location P02 had not considered — **iCloud Drive**
(`~/Library/Mobile Documents/…`), holding at least five further deployed databases.

**`FACT VERIFIED` — three further distinct deployed databases**, each confirmed from its own manifest:

| Database | Generation | Journal lines | **COGS** |
|---|---|---|---|
| `iMSCG` | **16.0+e** | 1,083 | **0** |
| `pankhamhom` | **18.0+e-20250223** | 956 | **0** |
| `T805efaplus` | **18.0+e-20250223** | 0 | **0** |

**`FACT VERIFIED` — TC-02 SURVIVES ITS SIXTH POPULATION EXTENSION — AND THE PATH SET IS NOW CLOSED
(see `28`).** **17 distinct deployed databases keyed on `database.uuid`, FOUR generations (14.0 newly
found), 2,553,914 journal lines — zero cost-of-sales entries in every one, every zero
injection-controlled.**

**`FACT VERIFIED` — the population is OPEN and P02 no longer publishes a total.** Every count published so
far — 5, 6, 8/5, 16/7 — has been superseded. The sweep was still running when this file was written.
**P02's position is now the invariant, not the count:** *no deployed database yet tested, on any
generation, contains a cost-of-sales journal line.*

## 7. Two Controls Applied To Results P02 Likes

P04 supplied the rule: **a test run only when it confirms is not a test; the control belongs on the
results you like.** Applied to P02's headline:

**`FACT VERIFIED` — SC-05. The zero-COGS instrument is positively controlled.** Taking a real 40,353-row
extract, the counter returns **0**. Injecting **one** synthetic cost-of-sales row into the same data and
re-running the same counter returns **1**. **The instrument can see a cost line and returns zero because
there are none — not because it cannot see them.** This control had never been run before; the headline
had gone six databases without one.

**`FACT VERIFIED` — SC-06. The symlink trap does not inflate P02's sweep.** `/Volumes/iMac` **is** a
symlink to `/` on this host, as P04 reported. P02's sweep used a non-following `find`, and **0 of its
results lie under that path** — verified rather than assumed.

## 8. Peer Handling

| Item | Disposition |
|---|---|
| P04's two traps | **Both verified independently.** The symlink is real and did not affect P02 (§7); the seven-snapshot/one-identity point P02 had already found independently by uuid. |
| P04's census total | **Not adopted**, as P04 advised and as P02 already practises. P02 also does not adopt P07's reported 15/7/3. **Two independent sweeps agreeing on 7 identities and 3 generations is corroboration; the file counts differ and should.** |
| P04's rule | **Adopted and applied** — §7. |
| P04's withdrawal of its own confirmation | Noted as the mirror of P02's result and as the better outcome of the two: P04 ran the control, the control cost it a confirmation, and it withdrew. |
| Returned to P04 | The source-scope check they suggested — run, and it refuted a published P02 absence (§4). |

---

## 9. Second Peer Exchange — Two v18 Databases Analysed, Not Merely Counted

A further P04 message identified that two of the three databases P02 had only **counted** for cost-of-sales
lines are materially different from each other and from the first. Both were analysed. **This produced the
strongest replication in the package and a proper control for its headline.**

### 9.1 `pankhamhom` — an independent replication of the deployed cost shape

**`FACT VERIFIED` — SC-07.** Odoo **18.0**, 3 companies, 478 modules, 956 journal lines.

| Measure | Result |
|---|---|
| `anglo_saxon_accounting` | **false** in all 3 companies |
| Categories with **real-time** valuation | **6 of 13** |
| Valuation layers | **201**, total value 2,294,006.95 |
| **Layers carrying a journal entry** | **124** — the valuation-to-accounting path **is firing** |
| Configured stock **output** accounts | **3**, ids 21 / 907 / 1084 |
| **Type of all three** | **`expense_direct_cost`** |
| **`reconcile` on all three** | **`false`** |
| Valuation accounts | 2, both `asset_current` |
| **COGS lines** | **0** of 956, counted with the positively-controlled instrument |

**`FACT VERIFIED` — SC-08. This is `iSMEs`'s shape, reproduced independently on a different generation and
a different business.** Split recognition off, real-time valuation on, outbound stock accounts typed as
**expense**, and **not reconcilable** — so cost is recognised **at delivery**, straight to expense, with
**no interim position and no matching possible even in principle**.

**`TC-16` was a single-database fact. It is now replicated:** *every* configured outbound stock account in
*every* deployment examined — eight in `iSMEs` (16.0), three in `pankhamhom` (18.0) — is an expense account
flagged **not reconcilable**. Eleven accounts, two generations, two businesses, no exception.

**Stated with restraint:** 77 of the 201 layers carry no journal entry. **This is not offered as a
finding** — 7 of the 13 categories have no valuation mode set, and layers on those legitimately produce no
entry. Separating them needs the category join performed in `22` §14.2 for the other database, and it was
**not** run here.

### 9.2 `T805efaplus` — the control the zero-COGS invariant needed

**`FACT VERIFIED` — SC-09.** Odoo **18.0**, 1 company, 123 modules, **87 categories all with no valuation
mode set, 0 valuation layers, 0 journal lines.** A never-transacted v18 install.

**Its value is as a negative control**, and it closes a gap in P02's headline that no amount of extra
databases could:

| Identity | Generation | Inventory actually valued? | Valuation entries posted? | **COGS** |
|---|---|---|---|---|
| `T805efaplus` | 18.0 | **no — never transacted** | 0 | **0** |
| `idemo18_uat` | 18.0 | 47,801 layers | **0** — valuation mode unset on all 126 categories | **0** |
| `pankhamhom` | 18.0 | 201 layers | **124** | **0** |
| `iSMEs` | 16.0 | 74,982 layers | **57,863** | **0** |

**`FACT VERIFIED` — SC-10. The zero is not an artefact of inactivity.** Two deployments moved real valued
inventory **and posted the valuation entries** — 57,863 and 124 of them — and still produced **no
cost-of-sales line**. The control case shows what a genuinely empty database looks like, and it looks
different. **The zero is a property of the mechanism, not of the data volume.**

**And the three v18 identities happen to cover all three discriminating configurations:**
never-transacted; gate **on** with valuation **off**; gate **off** with valuation **on**. P02 did not
assemble that set — a peer did, by correcting the population twice.

### 9.3 Source scope — a second and third data point

| Database | Installed | In P02's declared v18 root | **Absent** |
|---|---|---|---|
| `idemo18_uat` | 361 | 295 | **66 (18%)** |
| `pankhamhom` | 478 | 412 | **66 (14%)** |
| `T805efaplus` | 123 | 114 | **9 (7%)** |

**`FACT VERIFIED` — SC-11.** The gap is not peculiar to one deployment. `pankhamhom`'s absent set again
includes **`account_payment_multi_deduction`**, directly on P02's settlement analysis.

**`FACT VERIFIED` — SC-12, and this is P04's framing, adopted.** P04 measured **27** absent modules against
the same database where P02 measured **66**. **The difference is entirely in the two declared source sets,
not in the deployment.** Therefore:

> **Neither declared source scope contains what runs, and the two numbers are not comparable to each
> other.** The only sound joint statement is the qualitative one. P02 will not publish its 66 as though it
> were a property of the deployment; it is a property of P02's declared root.

### 9.4 A property of the withdrawn absence, worth recording as method

P04 observed of P02's withdrawn `VERIFIED ABSENCE` (§4) that **a reader auditing it would have confirmed
it** — the search was correctly specified, correctly executed, and correctly reported over the root it
named. **It survives exactly the check designed to catch it.**

**`SUPPORTED INTERPRETATION`.** That is the most dangerous shape a negative claim can take, and no amount
of re-running the stated pattern would ever expose it. **Only comparing the declared scope against what the
system actually runs does** — which is a different kind of check from the one this package performed on its
negatives throughout. It is recorded here rather than in a lessons file because it bears directly on how
the remaining source negatives in `01`–`11` should be read.

### 9.5 What P02 adopted, and what it did not

| Item | Disposition |
|---|---|
| The two databases' relevance | **Adopted** — and analysed, not accepted. Every figure above was derived by P02 from the archives. |
| P04's "neither scope contains what runs" framing | **Adopted** — §9.3. |
| P04's "survives its own audit" observation | **Adopted** — §9.4. |
| P04's census, and P07's | **Not adopted.** Unchanged position. |
| P04's analytic-cancellation finding | **Not adopted and not assessed** — it is P04's domain, and P02 has no basis to evaluate it. |

---

## 10. Instrument Controls Run Against P02's Own Negatives

A third peer exchange reported two **instrument** failures rather than reasoning failures — a tree-hash
comparison that returned *"42 identical copies"* because shell **word-splitting on paths containing
spaces** had sent it to directories that do not exist, and a clean-room scrub whose hits were the substring
`ast` inside ordinary English words.

**Both classes apply directly to P02**, whose evidence roots are
`/Volumes/iMacSys/CLAUDE AI/…` and whose package sits under `…/SMEsPlus ENTERPRISE SUITE/…` — **paths full
of spaces** — and whose Layer-1 clearance rests on a scrubber that has only ever reported **zero**. Both
were tested.

### 10.1 Word-splitting — does not apply here, and the reason matters for anyone re-running this

**`FACT VERIFIED` — SC-13.** This host's shell is **zsh**, which does **not** word-split unquoted parameter
expansions. Tested directly: a directory named with a space, expanded unquoted, yields **one** argument,
not two, and an unquoted search over it returns the same result as a quoted one.

**P02's negatives are therefore not void from this cause.**

**But the portability caveat is real and is recorded for the next reader:** **bash *does* word-split.**
Every command in this package that expands a spaced path unquoted is **safe as executed and unsafe if
re-run under bash** — where it would search nothing and return a zero indistinguishable from a true
absence. **Any re-derivation of a P02 negative must either quote every path or state the shell.**

> P04's formulation is the one to keep: **an empty result and a unanimous result are the same shape.**
> A search that reached nothing and a search that found nothing are indistinguishable in the output, and
> only a positive control separates them.

### 10.2 The Layer-1 clean-room scrubber — now positively controlled

`14` §5 and every commit since have reported the Layer-1 handoff as carrying **zero** vendor tokens. That
zero had never been shown to be capable of being non-zero.

**`FACT VERIFIED` — SC-14.** Run on the real file, the scrubber returns **0**. Append **one** line
containing three vendor tokens to a copy of the same file and the same scrubber returns **1**.

**The scrubber fires when a token is present.** The Layer-1 clearance is now instrument-controlled rather
than asserted.

### 10.3 The v19 structural absence — now two-sided

The package's most load-bearing source claim is that the valuation-layer model **does not exist in v19**.
It carried one control. It now carries two, both re-run:

| Query | Result |
|---|---|
| the model name, in **v19** | **0** |
| the model name, in **v18** — same command, same quoting | **1** — *the pattern can match* |
| a model that must exist, in **v19** — same root | **1** — *the root is searchable* |

**Neither a dead pattern nor an unreachable root can produce this shape.** The absence stands.

## 11. How The Discriminating Set Came To Exist

Worth recording because it is not a property of either party's method.

The four-identity set that finally controlled P02's headline — never-transacted; gate **on** with valuation
**off**; gate **off** with valuation **on**; and a high-volume prior generation — **was assembled by
neither session.** Two of its three v18 members reached P02 because a peer corrected P02's population,
**after** P02 had corrected that peer's.

**`SUPPORTED INTERPRETATION`.** It is the residue of **reciprocal correction**, not of either denominator
discipline. Both sessions independently declared POPULATION, PATTERN and UNIT and both left PATH SET
unvalidated; each found the other's gap and neither found its own. **That is an argument for the exchange
being a control in its own right** — and it belongs in the method record rather than being claimed as a
result of P02's process, which did not produce it.

---

## 12. Third Peer Exchange — An Onchange Lead, Tested On P02's Own Disabling Setting

> ## ⚠ CORRECTION BANNER — §12 CHALLENGED AND CORRECTED (`C-37`, `C-38`, `C-39`; AAS-03 Expert 4)
>
> **`SC-17` over-generalised — `C-37`.** "The guard is **one-directional**" is false of the *method*.
> `stock_account/models/product.py:972-976` holds a **second raise, outside the `real_time` branch**,
> which evaluates unconditionally: the valuation account may not equal the input or output account.
> On the exact `idemo18_uat` state `SC-17` cites (accounts set, valuation NULL), **that branch does
> evaluate and can fire.** Only the *account-completeness* branch is one-directional. §12 quoted the
> first branch and attributed its property to the whole guard — **the aggregation failure `SC-19`
> names, recurring inside the section that names it.**
>
> **`SC-18`'s table was not whole-tree — `C-38`.** It was described as "**Two-sided, whole-tree**" and
> reproduces only under an **undeclared `--include='*.py'` filter**. Executed both ways:
>
> | measured | whole tree v18 | whole tree v19 | `*.py` v18 | `*.py` v19 |
> |---|---|---|---|---|
> | guard message string | **44** | **2** | 1 | 0 |
> | `property_valuation` | 106 | 103 | 39 | 37 |
>
> The two v19 hits are obsolete `#~` msgids in `i18n/zh_TW.po` and `i18n/es_419.po`, so the **verdict
> survives** — but the published description is not the executed measurement, against this package's
> own *publish the command, not the pattern* standard.
>
> **`P02-F-05c` mis-attributes the change — `C-39`.** v19 did not merely remove a guard: it removed
> **the fields the guard protected**. `property_stock_account_input_categ_id` and
> `…output_categ_id` have **zero non-test `.py` occurrences** in the v19 root, and the v19
> `product.category` declares only `property_stock_valuation_account_id` and
> `property_price_difference_account_id`. Category-level interim in/out accounting was **replaced** by
> `res_company.inventory_valuation` plus per-company `ir.default` writes. The published sentence
> ("selecting perpetual valuation no longer requires the stock accounts to exist") is literally true;
> the design conclusion must be restated **against the replacement mechanism, not against an absence**.
>
> **Also accepted, not yet executed (`C-40`):** `SC-16`'s `REFUTED` verdict on the combo-tax handler is
> **scoped to the sale-order route only**. The direct customer-invoice route
> (`account/models/account_move_line.py:878-886`) applies `product_id.taxes_id` with **no combo test**,
> and `P02-F-07` establishes invoices exist independently of orders. The verdict should read *"refuted
> on the SO path; unrefuted on the direct-invoice path"*. **The P04 defect class survives there.**

P04 reported that the routine forcing an equipment-flagged product to non-storable with serial
tracking is an `@api.onchange`, which "binds only in the form. Any import, script or programmatic
write sets the equipment flag without it firing", and put the question to P02 directly: *given
`property_valuation` unset on 126 categories was your disabling setting, an on-change that never
fires on the import path is worth a look on your side too.*

That is the same defect class as P02's own `RE-04` / `EV-P02-070` (delivered quantity read-only in
the UI, writable at the data layer). It was tested. **The lead does not apply to
`property_valuation` — and testing it refuted a P02 statement in the opposite direction.**

**`SC-15` — the instrument, and its control.** An AST pass over each module's Python, selecting
functions carrying an `@api.onchange` decorator whose body **assigns** to a `self.<field>` matching
the accounting-relevant set (valuation, cost method, standard price, invoice policy, anglo, stock
input/output/valuation accounts, storability, tracking, fiscal position, taxes, journal, account).
A decorator that only *warns* is not an assignment and is not counted.

`PATH SET` — the two declared source roots. `PATTERN` — the AST predicate above, not a text grep.
`UNIT` — one handler. **Control:** a synthetic module containing one `@api.onchange('kind')` whose
body is `self.property_valuation = 'real_time'` was placed outside both roots and passed to the same
instrument. It **reported 1**. The instrument fires on the exact shape being looked for.

**`SC-16` — result on the O2C path.** Across `sale`, `sale_stock`, `stock`, `stock_account`,
`account`, `product` in v18: **three** `@api.onchange` handlers in `stock_account/models/product.py`
touch cost settings (`standard_price` ×2, `property_cost_method` ×1) and **all three are
warning-only** — they return a `warning` dict and assign nothing. **Seven** handlers in the path
assign an accounting-relevant value, of which exactly one is reachable in O2C:
`account/models/product.py:135 _onchange_type`, which clears `taxes_id` and `supplier_taxes_id` when
a product's type is `combo`.

**That one is `REFUTED` as an exposure.** `sale/models/sale_order_line.py:512-514` sets
`line.tax_id = False` for `product_type == 'combo'` in the line's own compute, independently of the
product's stored taxes. A combo product imported with taxes still carries them on the product record,
but they cannot reach a sale line. The form-only handler is real; its bypass has no accounting effect
on this path.

**A whole-tree pass found exactly one handler anywhere that assigns `is_storable` or `tracking`** —
`stock/models/stock_quant.py:952`, the inventory-adjustment form. **P04's handler is not in either
declared source root, and the tokens naming it appear nowhere in the roots searched.** Consistent
with `RE-23`: the modules that would carry it are among those absent from this host. **It is
therefore neither confirmed nor disputed here, and is not adopted.**

**`SC-17` — the correction this produced. A P02 statement is too strong.** Looking for an onchange on
`property_valuation` found instead an `@api.constrains`:

`stock_account/models/product.py:964-976`, `_check_valuation_accounts`, decorated
`@api.constrains(lambda self: tuple(self._get_mandatory_stock_account_property_field_names() + ['property_valuation']))`:

```python
if category.property_valuation == 'real_time':
    if any(not category[account] for account in fnames):
        raise ValidationError(_('The stock accounts should be set in order to use the automatic valuation.'))
```

A constraint, not an onchange — **it fires on create and write, including imports and scripts**. So a
cross-validation between two of the settings that determine cost recognition **does exist in v18**,
and `22_P02_TARGETED_CLOSURE_DEPLOYED_EVIDENCE.md` §13, which said *"no cross-validation exists
between the settings that jointly determine the outcome — in either generation"*, is **refuted for
v18**. Corrected in place; logged as `RE-24` / `C-33`.

**Four other statements of the same family survive, and the distinction is the point.**
`01_P02_PROCESS_MAP.md:169`, `21_P02_DEPLOYED_DATABASE_EVIDENCE.md:54` and `:91`, and
`17_P02_AAS_PLUS.md:130` each name the pair as **a boolean on the company and an account on the
product category**. The guard found here is **internal to the category** and does not reference
`res_company.anglo_saxon_accounting` at all. Those statements are correct as written.

**What survives, sharpened rather than weakened.** The guard is **one-directional**: it fires only
when `property_valuation == 'real_time'`. Accounts configured with valuation left unset raise
nothing. **That is precisely the state of `idemo18_uat`** — accounts set, `property_valuation` NULL
on all 126 categories, 47,801 valuation layers, zero cost of sales. And the unset state is **the shipped
default asserting itself**: the field carries no Python `default=` (`EV-P02-046`), but
`stock_account/data/stock_account_data.xml:5` installs an `ir.default` of **`manual_periodic`**
(`EV-P02-100`). A category with no override therefore resolves to **manual**, not to nothing — so the
126 NULL categories are what the product ships as, not an implementer's error (`EV-P02-117`). The designers paired these two settings and guarded
one direction of the pair; the deployed defect sits in the direction they left open. **A guard that
exists and is asymmetric is stronger evidence than no guard at all.**

**`SC-18` — v19 removes the guard, on the target generation.** Two-sided, whole-tree:

| Measured | v18 | v19 |
|---|---|---|
| Files containing `_check_valuation_accounts` | **1** | **0** |
| Files containing the guard's message string | **1** | **0** |
| Files containing `property_valuation` | 39 | 37 |

The zero is the **guard**, not the field — the field is still there in comparable breadth, which is
what the third row controls for. In v19 the mode is resolved by a two-level fallback,
`stock_account/models/product.py:73-77`:

```python
product_template.valuation = product_template.categ_id.with_company(
    product_template.company_id).property_valuation or self.env.company.inventory_valuation
```

**`FACT VERIFIED` — P02-F-05c.** On v19, selecting perpetual valuation **no longer requires the stock
accounts to exist**, and the setting can be satisfied by a company-level default the category never
names. The one cross-validation that existed over the cost-recognition configuration is **absent from
the generation SMEsPlus targets**.

**Scope note, `CORR1`.** That single expression reads the category `with_company(product_template.company_id)`
but takes the fallback from `self.env.company` — **two different company sources in one resolution**.
For a product with no `company_id` the category is read with `with_company(False)` while the fallback
still resolves against the acting company. Registered against the COMPANY scope in
`20_P02_SCOPE_OWNERSHIP_MATRIX.md` as an observation, **not** as a defect: no deployed instance was
tested against it.

**`SC-19` — and the first draft of this section was itself wrong.** It closed by saying the guard had
been sitting unread. **It had not been.** `EV-P02-045` cites `product.py:964-970` directly, and
`00_README_PACKAGE_INDEX.md` §3b states the rule in plain words — *real-time valuation cannot even be
switched on until three stock accounts exist*. The package **had** the fact, registered and prominent.

**So the defect is not a missed reading. It is an internal inconsistency that survived publication:**
`00` §3b asserts the guard, and `22` §13 asserts *no cross-validation exists … in either generation*.
**Both statements were in the same package, and neither round of adversarial challenge put them in the
same room.** That is the package's own characteristic failure recurring — `RE-07` (a total that did not
reproduce from its table), `RE-10` (one defect counted three times): **not citation, but aggregation.**
Two correctly-cited facts, generalised into a summary claim that contradicts one of them.

**Method note.** The correction came from P04's lead **not applying**. Their specific handler could not
be verified here at all. What produced the finding was executing a check whose answer was expected to
be *no* — and reading what was next to the answer. **A lead worth running is not the same as a lead
that is right**, and two of the five identifiers this section first issued were **duplicates of P02's
own existing evidence**, withdrawn above.
