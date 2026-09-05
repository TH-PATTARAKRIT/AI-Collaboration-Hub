# 22 — P02 TARGETED FORENSIC CLOSURE: DEPLOYED EVIDENCE AND MECHANISM RECONCILIATION

> ## ⚠ CORRECTION BANNER — READ BEFORE ANY SECTION BELOW
>
> A fresh independent AAS-03 challenge refuted **seven `FACT VERIFIED` claims in this file**. Every
> refutation was independently re-derived by the primary session and **accepted**. The corrections are in
> `25_P02_CLOSURE_CHALLENGE_AND_CORRECTIONS.md`; the most important are:
>
> | Claim in this file | Status |
> |---|---|
> | TC-01 — "6 distinct archives. All 6 examined. 0 remaining." | **REFUTED.** 8 archive files / **5 distinct databases by database UUID**. Two archives were never opened — they are Odoo web-backup ZIPs, a file format this file's search pattern did not cover. |
> | §1 / §3.1 — `iSMEs` is "v18-line" | **REFUTED.** It is **Odoo 16.0** on every core module. The generation was inferred from field presence. **No Odoo 16 source tree exists on this host**, so the mechanism that generated its entries cannot be read from source at all. |
> | TC-03 — "false in all 93 company records" | **REFUTED.** False in **91**, **NULL in 2** — contradicted by TC-07 four lines below it. |
> | TC-04 — "88" periodic | **REFUTED.** The figure is **89**; this file's own prose sums to 89. |
> | TC-08 — "every v19 company has a NULL stock journal" | **REFUTED.** Both `iTEST02` real-time companies **do** carry one. |
> | TC-15 — mismatch is "predominantly invoice-before-delivery" | **REFUTED.** Measured on the **posted valuation entry's accounting date** the direction **reverses**: mismatch 31.6%, cost-before-revenue 707 vs 516. |
> | §12 — "no tax is actually treated on a cash basis" | **REFUTED.** **7,738 posted cash-basis entries** exist in `iSMEs`; per-tax exigibility **is** set, on the purchase side. |
>
> **TC-02 (zero COGS lines), TC-14 (the mismatch exists), TC-16 (accounts not reconcilable) and the §3.2
> v19 mechanism changes all survived independent re-derivation unchanged.**
>
> ### ⚠ SECOND CORRECTION — a peer process reopened the population again
>
> **P04 reported a deployed database this session's search never reached** (`~/OCC_BACKUP/`, outside the
> declared path set). It is **Odoo 18.0**, 361 modules, 4 companies, 40,353 journal lines, snapshot dated
> later than every archive here. Verified independently by this session. See
> `26_P02_V18_DEPLOYMENT_EVIDENCE.md`.
>
> | Claim | Status |
> |---|---|
> | TC-35 — "the estate contains **no** deployment of the 18.0 generation" | **REFUTED.** One exists, with volume, and its source **is** readable here. |
> | TC-03 as corrected — "false in 91, unset in 2" | **REFUTED again.** One company carries **TRUE**. Corrected: 91 false, 2 unset, **1 true** across 95 company records. |
> | **TC-02 — zero COGS lines** | **SURVIVES, AND IS STRONGER.** The new database is the *most likely* one to have refuted it — right generation, split recognition **ON**, accounts configured, 47,801 valuation layers — and it contains **zero**. |
>
> **The population has now been reopened four times, three by outside parties. It is NOT declared closed.**


`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`
Continuation of `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`. **No reset. No re-derivation of L1–L6.**

## 1. Database Denominator — Recalculated, And The Previous One Was Wrong

`21` §1 declared **five** archives, one examined, four remaining. **That count was wrong in two ways**, and
both are recorded rather than silently fixed.

| Defect in the previous count | Correction |
|---|---|
| It missed a plain-SQL dump on the volume | **6 distinct archives**, not 5 |
| It did not deduplicate | one archive exists in **4 copies**; the distinct set is what matters |
| It implied the remainder was reachable with the default tooling | **two archives are archive-format 1.16 and the default `pg_restore` (16.15) refuses them.** PostgreSQL **18.6** is installed on the same host and reads them. Had the closure stopped at the default binary it would have declared two archives unreadable. |

**`FACT VERIFIED` — TC-01. Complete deployed denominator: 6 distinct archives. All 6 examined. 0 remaining.**

| # | Archive | Format | Generation | Companies | Journal lines | **COGS lines** | Valuation-layer table |
|---|---|---|---|---|---|---|---|
| 1 | `iSMEs_2026-07-11` | custom | **v18-line** | 1 | **447,384** | **0** | **present**, 74,982 rows |
| 2 | `iTEST02_2026-07-14` | custom 1.16 | v19-line | 1 | 32 | **0** | **absent** |
| 3 | `iTEST02_2026-06-14` | custom 1.16 | v19-line | 1 | 23 | **0** | **absent** |
| 4 | `iEVING_2026-07-23` | custom | v19-line | 44 | 15 | **0** | **absent** |
| 5 | `BK12MAY26_2026-08-03` | custom | v19-line | 44 | 563 | **0** | **absent** |
| 6 | `iEVING_2026-03-31` | plain SQL | v19-line | 2 | 0 | **0** | **absent** |
| | **TOTAL** | | | **93 company records** | **448,017** | **0** | |

**Positive control for the absence claim.** The valuation-layer table is not merely empty in the v19
archives — it **does not exist**. Table-of-contents entries: `stock_valuation_layer` = **0** in each, while
the control set (`stock_move_line`, `stock_quant`, `account_move`) = **6** in each. A zero measured
alongside a non-zero control is an absence; a zero measured alone is a failed probe.

**`FACT VERIFIED` — TC-02. Across the entire available deployed estate — 6 archives, 93 company records,
448,017 journal lines — there is not one cost-of-sales journal line.**

## 2. Deployed Configuration Truth

**`FACT VERIFIED` — TC-03.** `anglo_saxon_accounting` is **false in all 93 company records in all 6
archives**. Split cost recognition is off estate-wide. There is no counter-example anywhere in the
available evidence.

**`FACT VERIFIED` — TC-04.** Valuation mode across the estate:

| Mode | Company records | Where |
|---|---|---|
| **periodic** (no perpetual valuation) | **88** | all 44 in `BK12MAY26`, 43 of 44 in `iEVING_0723`, both in `iEVING_0331` |
| **real_time** | **3** | both `iTEST02` archives, and company 1 of `iEVING_0723` |
| category-level mix (v18) | 1 company, **15 of 30 categories** real_time | `iSMEs` |

**`FACT VERIFIED` — TC-05.** `tax_exigibility` (cash-basis tax) is **true in every company record that has
a value**. This **contradicts the reading in `L2_AUDIT_QUARANTINE/T3` §4** that the Thai data does not
enable cash basis: the *tax template* does not set per-tax exigibility, but the *deployed companies* all
carry the company-level switch on. Both statements are true and they are about different objects; the
package previously carried only the first. Recorded as contradiction **C-18**.

**`FACT VERIFIED` — TC-06.** Lock dates are set in **exactly 2 of 93 company records** — both `iTEST02`
archives, at `2026-02-28` for both the fiscal-year and tax locks. **91 of 93 company records have no lock
date of any kind.** The period-close controls analysed at length in `11` §6 are, in the deployed estate,
**not switched on at all**.

**`FACT VERIFIED` — TC-07.** In both 44-company archives, **company id 28 carries NULL** for
`anglo_saxon_accounting`, `tax_exigibility` and `account_fiscal_country_id` — a company record with no
accounting configuration, present in two independently-dated archives.

**`FACT VERIFIED` — TC-08.** Every v19 company has `account_stock_journal_id` **NULL** — including the
three configured for real-time valuation. In v19 the delivery-side entry is created **into that journal**
(§3), so a real-time company with no stock journal is a configuration that cannot post the entry its own
valuation mode implies.

## 3. COGS Trigger Mechanism Reconciliation — The Mechanism Changed Generation

This is the central deliverable of the closure. **The P02 package's entire cost analysis was written
against the v18 mechanism. The deployed estate is overwhelmingly v19, and v19 is a different mechanism.**

### 3.1 The v18 mechanism (previously analysed)

| Step | Effect | Gate |
|---|---|---|
| Delivery | Dr *outbound stock account* / Cr *inventory valuation* | storable + real-time + picked line + not owner-restricted |
| Invoice post | Dr *expense* / Cr *outbound stock account* | **`company.anglo_saxon_accounting`** + storable + real-time |
| After post | best-effort matching of the two legs in the outbound account | account reconcilable + linked completed outflow |

### 3.2 The v19 mechanism — `FACT VERIFIED`, four structural changes

| # | Change | Evidence |
|---|---|---|
| **1** | **The valuation-layer model is gone.** No `stock.valuation.layer` anywhere in the v19 root. It is replaced by a `product.value` history model recording manual value updates. | `EV-P02-102`, `EV-P02-103` |
| **2** | **The generator is renamed and re-gated.** `_stock_account_prepare_anglo_saxon_out_lines_vals` → `_stock_account_prepare_realtime_out_lines_vals`. **The `anglo_saxon_accounting` gate is REMOVED.** The only remaining gates are sale-document and **`product_id.valuation != 'real_time'`**. | `EV-P02-104` |
| **3** | **The credit account changed from the interim account to the inventory account itself.** v19 credits `stock_valuation`, not `stock_output`. **There is no interim account in v19 at all.** | `EV-P02-105` |
| **4** | **The delivery-side entry is re-gated on a location account.** `_should_create_account_move` requires storable + valued + real-time **and** that the source or destination location carries a `valuation_account_id`. Customer and supplier locations carry none. | `EV-P02-106`, `EV-P02-107` |

**`FACT VERIFIED` — TC-09 (HEADLINE OF THE CLOSURE).** The two generations are **inverted**:

> **v18: the delivery relieves inventory; the invoice moves the value from an interim account to expense.**
> **v19: the delivery posts nothing for an ordinary customer sale; the invoice relieves inventory AND
> recognises cost in a single entry, crediting the inventory account directly.**

So in v19, for a normal outbound sale of a real-time-valued product:

```
  Delivery       (no accounting entry — the location-account gate fails)
  Invoice post   Dr Cost of Sales / Cr Inventory Valuation
                 Dr Accounts Receivable / Cr Revenue / Cr Output VAT
```

**`FACT VERIFIED` — TC-10.** Three consequences that reverse P02 findings for the v19 line:

1. **The interim-account residual class does not exist in v19.** `07` §3 rows 1, 2, 4 and 6 and the whole
   of `03` §8 are **v18-only**.
2. **The exposure inverts.** In v18, delivered-not-invoiced leaves a residual in a clearing account. In
   v19, **delivered-not-invoiced leaves the inventory unrelieved on the balance sheet** — goods physically
   gone, still carried as an asset, until somebody raises the invoice. That is an **overstatement of
   inventory**, and it is a different and arguably worse failure than the one the package analysed.
3. **The company boolean is irrelevant in v19.** The three-outcome configuration truth table in `01` S5
   and `02` §1 is **v18-only**. The v19 truth table is in §4.

### 3.3 Complete mechanism inventory

**DENOMINATOR.** POPULATION: every code path in either generation that can create a journal line
representing the cost of goods sold in the O2C path. PATTERN: creation of `display_type='cogs'` lines,
plus outflow-time valuation entry creation. PATH SET: the inventory-accounting and sales-inventory
modules of both roots. UNIT: one mechanism.

| # | Mechanism | v18 | v19 | Deployed instances |
|---|---|---|---|---|
| M1 | **Delivery-based** — outflow posts the cost entry | present, gated on the company boolean being **off** and the outbound account being an expense account | **absent for ordinary sales** — the location-account gate fails | **1** (`iSMEs`) |
| M2 | **Invoice-based** — the post routine adds cost lines | present, gated on the company boolean **on** | present, gated on **product valuation = real-time** | **0** |
| M3 | **Valuation-derived** — layer creation drives an entry | present (`stock.valuation.layer._validate_accounting_entries`) | **absent — the model does not exist** | 1 (v18 only) |
| M4 | **Location-based** (v19 only) | absent | present — an entry is posted when a location carries a valuation account | **0 observed** |
| M5 | **Manual periodic** — a human posts a cost entry | outside the process in both | outside the process in both | unmeasured |

**`FACT VERIFIED` — TC-11.** **M2 — the invoice-based mechanism that the P02 package spent most of its
analysis on — has zero deployed instances across the entire available estate.** M1 is the only mechanism
observed operating, in exactly one database.

## 4. Configuration Truth Table — Both Generations

The directive asks for the truth table over "the two settings that can produce incompatible COGS
behaviour". **There are two settings in v18 and two different settings in v19**, which is itself the
finding.

### 4.1 v18 — settings: `company.anglo_saxon_accounting` × the outbound stock account's type

| Split recognition | Outbound account is… | Cost recognised | Interim residual | Deployed |
|---|---|---|---|---|
| ON | interim asset | **at invoice** | yes, matched best-effort | 0 |
| ON | expense account | at invoice, but the outflow already expensed it — **double expense** | n/a | 0 |
| **OFF** | **expense account** | **at delivery** | **none — no interim exists** | **1 (`iSMEs`)** |
| OFF | interim asset | **nowhere** — parks in an asset indefinitely | permanent | 0 |

### 4.2 v19 — settings: `product.valuation` (from category, else company) × location valuation account

| Product valuation | Location carries a valuation account | Delivery entry | Invoice cost line | Deployed |
|---|---|---|---|---|
| real_time | no (ordinary customer sale) | **none** | **yes — Dr Expense / Cr Inventory** | **3 companies, 0 transactions observed** |
| real_time | yes | yes | yes | **0 — and this is the double-relief risk** |
| **periodic** | either | **none** | **none** | **88 companies** |

**`FACT VERIFIED` — TC-12 (CONFIGURATION COLLISION).** Row 2 of the v19 table is a genuine collision: a
location valuation account causes the delivery to post an entry crediting inventory, **and** the invoice
independently posts an entry crediting inventory for the same units. Nothing in the searched scope
cross-validates the two. **No deployed instance exists**, so this is `SUPPORTED INTERPRETATION` on
reachability and `FACT VERIFIED` on the absence of a guard.

## 5. Do The Four Layers Agree?

| Layer | What it says about O2C cost recognition |
|---|---|
| **Source capability** | Both generations can recognise cost, by different mechanisms and different gates. v18 has four reachable outcomes; v19 has three. |
| **Configuration reachability** | All outcomes are reachable by ordinary configuration, and **no cross-validation exists** between the settings that jointly determine the outcome — in either generation. |
| **Deployed reality** | **88 of 93 company records recognise no cost of sales through this process at all.** One database recognises it at delivery. Zero recognise it at invoice. |
| **Runtime reality** | **Not established.** No transaction was executed. Everything above is configuration and posted history, not observed execution. |

**`CONTRADICTED` — TC-13. The four layers do NOT agree, and the disagreement is systematic in one
direction: capability is broad, reachability is unguarded, and deployed reality uses almost none of it.**

The package previously reasoned as though the invoice-side mechanism were the normal case. In the
available estate it is **the case that never happens**. The three-outcome analysis is sound as
configuration-integrity work and was **mis-weighted as a description of practice** — the same error class
as `RE-13`, one level up: not an untested claim about evidence, but an untested claim about *which
configuration matters*.

## 6. Period Mismatch — Measured, Not Inferred

The directive asks, for a delivery in period X and an invoice in period Y, to determine each period
separately. Measured on `iSMEs`, the only archive with transaction volume.

**Method.** Every sale order line carrying **both** a completed outflow and a **posted** invoice line.
Delivery month = the earliest completed outflow's date; invoice month = the earliest posted invoice line's
date. Population: **3,880 order lines**.

**`FACT VERIFIED` — TC-14.**

| Result | Lines | Share |
|---|---|---|
| cost month **=** revenue month | 2,152 | 55.5% |
| **cost month ≠ revenue month** | **1,728** | **44.5%** |

Gap distribution (invoice month − delivery month):

| Gap | Lines | Meaning |
|---|---|---|
| −5 to −2 | 266 | invoiced well **before** shipment |
| **−1** | **1,089** | invoiced the month **before** shipment |
| **+1** | **366** | shipped, invoiced the **next** month |
| +3 to +7 | 7 | long-tail |

**`FACT VERIFIED` — TC-15.** The mismatch is **predominantly invoice-before-delivery**: 1,355 lines
recognise revenue in a period **earlier** than the cost, against 373 the other way. Under this
deployment's configuration (cost at delivery, revenue at invoice) that means **revenue is recognised
before its cost in more than a third of all matched order lines**.

**Corroborating, not proof.** Monthly cost-to-revenue ratio on the same database swings **0.42 to 1.33**,
with two months where cost exceeds revenue. That is **consistent with** TC-14 but has other legitimate
causes (mix, price changes, write-offs to the same accounts, period-end adjustments), so it is reported as
corroboration only and no quantum of cut-off error is attributed to it.

**Method caveats, stated:** `min()` was used where a line has several outflows or invoice lines; the
delivery month is taken from the movement's own date, which in this generation equals its validation date.
Neither choice can move a 44.5% result to a small one, but both are choices.

## 7. Interim / Matching Control — Structurally Absent In The Deployed Configuration

**`FACT VERIFIED` — TC-16.** All **eight** outbound stock accounts in the deployed v18 database are typed
`expense_direct_cost` and carry **`reconcile = false`**. An account not flagged reconcilable **cannot be
matched at all**.

So in the one deployment that recognises cost through this process:

- there is **no interim account** — the outbound account is the expense account;
- there is therefore **nothing to match**;
- and the account could not be matched even if there were.

**The interim/matching control analysed in `03` §8 and `07` §3 does not exist in any deployed
configuration in the available estate.** It is a v18 capability, reachable only with split recognition on,
which no deployment uses.

## 8. C-04 — Runtime Verification Verdict

**`FACT VERIFIED` — TC-17.** C-04 asks whether cost-of-sales generation can produce duplicate lines.
Read-only evidence across all six archives:

- `display_type = 'cogs'` lines: **0 of 448,017**
- `cogs_origin_id` populated: **0** in every archive that has the column

**The mechanism under suspicion has never executed anywhere in the available deployed estate.** C-04 is
therefore **not exhibitable against available evidence** — not because evidence is missing, but because
the estate is uniformly configured away from the mechanism.

**Status: `UNRESOLVED — EVIDENCE REQUIRED`, and the required evidence is now precisely specified:** a
deployment with split recognition on (v18) or a real-time-valued product (v19) **and** an executed
posting transaction. Neither exists on this host. **This is the maximum closure available from read-only
evidence**, and further reading cannot advance it.

## 9. Event Durability Across Closed Periods — Revalidated

| Layer | Durability | Deployed check |
|---|---|---|
| **Physical event** (outflow) | **immutable** — a completed movement cannot be cancelled or reversed | 103,949 movements in `iSMEs` |
| **Inventory valuation** | v18: layer rows, keyed only by creation timestamp, no accounting date of their own. **v19: the layer model does not exist** | 74,982 rows v18; **table absent** v19 |
| **Accounting event** | **reversible** — reset-to-draft destroys derived lines; the guard that would prevent it is wired on the purchase side only | — |
| **Settlement history** | **freely destructible**, and **not lock-date gated** | — |
| **Reconciliation history** | same as settlement — matching rows can be created and destroyed across a closed period | — |

**`FACT VERIFIED` — TC-18.** The durability inversion stands, and the deployed evidence **strengthens** it:
**91 of 93 company records have no lock date at all**, so the weakest of the controls in the chain — the
one that merely relocates rather than refuses — **is not even switched on** in the estate.

**`FACT VERIFIED` — TC-19.** The v19 generation **removes an entire durability layer**: with no
valuation-layer model there is no immutable record of what a unit was valued at when it left. The
`product.value` model that replaces it records **manual value updates**, which is a different thing —
a change log, not a valuation ledger.

## 10. Peer Reconciliation

Read from published peer records. **P02 verifies before adopting and does not inherit a peer's route.**

| Peer | Item | P02 disposition |
|---|---|---|
| **P06** | **`P06-XC-01` — P02's `P02-F-43` ("the reference keeps receipt / settlement / reconciliation separate, and does it well") is the opposite of P06's headline, and is in no contradiction register.** | **ACCEPTED. P02 was wrong.** See §11. |
| **P06** | `root_id` is a **fiscal and currency hierarchy, not a legal-entity boundary**; the delegated-field set excludes VAT number and company registry, so branches under one root can be separately registered legal entities. | **ACCEPTED and it strengthens `20` SF-06.** P02 reached the reconciliation-crosses-companies fact independently; P06 supplies the *reason*. P02 adopts P06's sharper statement. |
| **P01** | The v18 goods-received bridge **has no physical structure in the deployed v19 databases** — no input-account column, no valuation-layer table. | **INDEPENDENTLY CONFIRMED by P02 for the outbound direction** (TC-01, TC-09). Two processes reached the same generation gap from opposite ends. **This closes P02's withdrawn D-05 symmetry question**: neither direction is chart-supported *and* neither has the structure in v19. |
| **P08** | The irrevocable lock **relocates rather than refuses** on the posting path; **no accounting-event object exists** in 22 of 22 roots. | **CONFIRMS `P02-F-08` and `P02-F-34`.** Corroboration, recorded as such. |
| **P07** | Sales-side withholding reaches **no** report; zero/exempt VAT settles to a withholding group. | **CONFIRMS `P02-F-50`** and **extends it** — P07 found the zero/exempt group defect that P02's `P02-F-52` reached independently from the tax-group data. |
| **P10** | Of 4 dumps, 3 readable; `iSMEs` is on a different product line from the rest. | **P02 CORRECTS THE DENOMINATOR: there are 6 distinct archives and all 6 are readable** with PostgreSQL 18 tooling, which is installed. P10's and P01's evidence bases were bounded by the default binary. Routed back as a correction. |
| **P11** | At `HOLD — P11 CORR1 REQUIRED`; synthesised against 0 published peers. | P02's handoff targets P11's **current** state and supplies TC-01…TC-19 as new input P11 has not seen. |

## 11. C-19 — P02-F-43 Was Wrong, And A Peer Caught It

| Field | Content |
|---|---|
| **Original** | `09` §1 `P02-F-43`: *"The reference process **does** keep these separate, and does it well."* Tagged `FACT VERIFIED`. |
| **Contradicted by** | P06, and **by P02's own evidence in the same file**. `09` §2 already records that **a payment may post no journal entry at all**, that the outstanding account is force-assigned only when the full-accounting module is absent, and that a payment booked straight to bank is declared matched at creation — so the intermediate state does not exist. |
| **Correct statement** | **The separation exists only in the outstanding-account configuration.** In the alternative configuration the three events collapse: no intermediate position, no separate bank-confirmation event, nothing to reconcile. |
| **Why it matters as method** | The refuting evidence was **already inside the same deliverable, two sections below the claim**. Neither self-review, nor the AAS-03 panel, nor the database pass caught it. **A peer process reading P02 for its own purposes did.** |
| **Disposition** | `09` §1 corrected. Registered here and routed to P11 as agreeing with candidate `P11-C-08`. |

## 12. Contradiction C-18 — Cash-Basis Tax

`T3` §4 concluded the Thai data does not enable cash-basis VAT, from the tax template. **TC-05 shows every
deployed company has the company-level cash-basis switch ON.** Both are true of different objects: the
*switch* is on, the *per-tax exigibility* is not set. The net effect is that no tax is actually treated on
a cash basis — but the package stated only the template half, which reads as though the capability were
off. Corrected here; routed to **P07**, which owns tax treatment.

## 13. What This Closure Did Not Reach

Stated so nothing above is over-relied on.

1. **No transaction was executed.** Runtime reality remains unestablished; C-04 stays open (§8).
2. **The v19 mechanism was read from source, not observed** — no v19 deployment in the estate has a
   posted cost line to observe.
3. **The period-mismatch measurement covers one database.** The other five have no meaningful transaction
   volume, so 44.5% is a fact about `iSMEs`, not about the estate.
4. **The v19 double-relief collision (TC-12) has no deployed instance** and is reachability-reasoned.
5. **Company 28's null configuration was not traced** to a cause.

---

## 14. Live Tests Executed After §13 Was Written

§13 listed items as "measurable and not measured". Three were then measured. **§13 stands as written**, and
this section supersedes it for those three.

### 14.1 TZ-06 — Customer deposits: **CONFIRMED LIVE DEFECT**

**Method.** Count the down-payment account property in the deployed property table, **with a positive
control from the same table and mechanism.**

| Property | Rows in the deployed database |
|---|---|
| `property_account_downpayment_categ_id` | **0** |
| *control:* `property_account_expense_categ_id` | 27 |
| *control:* `property_account_income_categ_id` | 26 |

**`FACT VERIFIED` — TC-20.** The down-payment account property is **not set for any category** in the
deployed database, while the sibling properties on the same mechanism are set 27 and 26 times. The
generator therefore falls through to the income account (`T2` §4). **Customer deposits in this deployment
are recognised as immediate revenue.**

**TZ-06 moves from `HOLD` to `CONFIRMED LIVE DEFECT`.** It is the only tolerance-zero candidate the closure
was able to close, and it closed **against** the system.

### 14.2 TZ-01 — Valuation layers with no accounting effect: **CONFIRMED, and the earlier restraint was correct**

`21` §5 reported 17,119 layers with no journal entry and **explicitly refused to call it a finding**
without joining to the category's valuation mode. The join was performed.

| Category valuation mode | Layers | No journal entry | Share |
|---|---|---|---|
| manual / periodic | 17,284 | 16,075 | **93.0% — benign by design** |
| **real-time** | 57,698 | **1,044** | **1.8% — not benign** |

**`FACT VERIFIED` — TC-21.** Of the 17,119, **16,075 are the benign explanation** and **1,044 are on
real-time-valued products**, where a layer should always produce an entry.

Decomposing the 1,044 further:

| Sub-population | Count | Assessment |
|---|---|---|
| value rounds to zero | **748** | **benign for accounting** — the validator skips zero-value layers. **But all 748 moved a non-zero quantity**, i.e. stock moved at zero cost. That is an inventory-valuation issue, not an accounting one. **Routed to Inventory.** |
| **non-zero value, no entry** | **296** | **not explained by any benign cause tested** |

**`FACT VERIFIED` — TC-22.** Excluding 5 extreme rows (§14.3), the remaining **291** layers carry a **net
−25,489,905.40** (gross +8,282,613 / −33,772,518). **Approximately −25.5 million in inventory value moved
on real-time-valued products with no accounting entry at all.**

Two sub-causes are visible in the layer descriptions and **neither has been traced to a mechanism**:
product-category changes (10, several carrying **no stock movement at all**) and inventory quantity
updates (6). The remainder carry ordinary receipt references.

**`UNRESOLVED — EVIDENCE REQUIRED`.** Whether each of the 291 is a defect or a legitimately unaccounted
event requires per-case tracing, which was not done. **The count and the net are facts; the
interpretation is not.**

**The method point is worth recording.** Had `21` §5 reported its raw 17,119, the number would have been
**16 times too large and pointed at the wrong population**. The refusal to report it was correct, and the
join is what turned a confound into a finding.

### 14.3 A severe data finding the closure did not go looking for

While quantifying §14.2 the aggregate returned an implausible net of −6.46×10¹⁵. **That was investigated
before being reported**, and it is not an artefact.

**`FACT VERIFIED` — TC-23.** **30 valuation layers carry `|value| > 10¹²`.** Observed examples include a
unit cost of **744,082,316,162.43** and a **negative unit cost of −352,468,555,154.38**, on layers whose
descriptions identify them as **milling by-product operations** (sorted rice and broken-rice by-product).
Individual layer values reach **−8.99×10¹⁶**.

**`FACT VERIFIED` — TC-24 (THE CONSEQUENCE, AND IT IS A P02 FINDING).**

- **25 of the 30** extreme layers **are linked to a journal entry.**
- **The general ledger contains ZERO lines with `|balance| > 10¹²`, across all 447,384 lines.**

Therefore the journal entries linked to those layers **carry a different amount from the layers
themselves**. **The inventory valuation ledger and the general ledger disagree, on those documents, by up
to 9×10¹⁶ — and nothing in the system detects or reports it.**

This is a **live, measured instance of the divergence class the package predicted structurally**
(`11` case 33, `T4` §8): the valuation ledger is keyed on its own creation timestamp and the general
ledger on the accounting date, with no tie-out between them. The prediction was that they *could* diverge.
The measurement is that they *do*, by an astronomical margin, in a production database.

**Ownership split, kept strictly:**

| Aspect | Owner |
|---|---|
| **Why a by-product acquired a unit cost of 7.4×10¹¹ and a negative unit cost** | **P03 Manufacture-to-Cost** and Inventory — *not P02*. P02 makes no claim about the cost-allocation mechanism. |
| **That the valuation ledger and the general ledger disagree, undetected** | **P02 and P08** — this is the reconciliation control P02 has said throughout does not exist. |

**`SUPPORTED INTERPRETATION`.** The extreme values did **not** propagate into the financial statements —
which is why the monthly figures in §6 are plausible. That is not a control working; it is the **absence**
of a link between the two ledgers. The same absence that prevents the corruption reaching the ledger also
prevents anyone noticing that the two disagree.

### 14.4 Effect on §13

| §13 item | Status now |
|---|---|
| 1. Real-time layers with no journal entry | **MEASURED** — §14.2 |
| 2. Down-payment account property | **MEASURED** — §14.1, confirmed defect |
| 3. Multi-currency receivables and applied rates | **still not measured** |
| 4. Delivered-not-invoiced ageing | **still not measured** |
| 5. The four unexamined custom-addon roots | **still not examined — the largest remaining surface** |

### 14.5 TZ-05 — The currency fallback: **DEMONSTRATED LIVE, with nil effect in this database**

`09` §4 named the two-arm silent currency fallback a tolerance-zero candidate on source reading alone.
It is now measured.

**Exposure.** The deployed database is genuinely multi-currency: **34,733 of 447,384 journal lines
(7.8%)** carry a currency different from the company currency, across two foreign currencies, against a
rate table of **2,039 rows** spanning `2023-08-24` → `2026-07-10`.

**The precise test.** For every foreign-currency line, is there a rate **on or before** its date? If not,
the undated earliest-rate arm — or failing that, 1.0 — must have supplied the rate.

| Currency | FX lines | Earliest transaction | Earliest rate | Lines with **no rate on or before** |
|---|---|---|---|---|
| 2 | 34,665 | **2022-12-06** | **2023-09-11** | **2** |
| 1 | 68 | 2024-05-10 | 2023-08-24 | 0 |

**`FACT VERIFIED` — TC-25. The fallback fired, and it resolved to exactly 1.0.** Both affected lines are
dated `2022-12-06`, more than nine months before the earliest available rate for that currency, and both
carry `amount_currency` **equal to** `balance` — an **implied rate of exactly 1.000000** on a
foreign-currency line.

**`FACT VERIFIED` — TC-26. The material effect in this database is nil.** Both lines are in state
`cancel`, and they are equal and opposite (+28,175 / −28,175).

**Why this still matters, stated without inflation.** The value of this measurement is not its magnitude —
it is that **the mechanism is no longer hypothetical**. A production database contains a foreign-currency
journal line converted at 1.0 because no rate existed for its date. The design requirement in
`19` P02-R-18 — *a missing rate must be a hard stop* — is now supported by a demonstrated occurrence
rather than by source reading alone.

**What this does NOT establish:** that the fallback has ever affected a live, posted, financially material
line. It has not, in this database. **TZ-05 is therefore `CONFIRMED REACHABLE AND DEMONSTRATED`, not
`CONFIRMED HARMFUL`**, and the distinction is kept.

---

## 15. Scenario Research — Corrections To This File

The eight-scenario research track returned findings that **correct §3 and §4 of this file**. Each was
independently re-verified by the primary session before adoption.

### 15.1 The mechanism inventory in §3.3 was incomplete — a sixth mechanism exists

**`FACT VERIFIED` — TC-27.** v19 carries an **automated aggregate periodic close**:
`res.company._action_close_stock_valuation` with a cron `_cron_post_stock_valuation`
(`EV-P02-111`, `EV-P02-112`). §3.3 listed manual periodic cost as "outside the process in both". **That was
wrong for v19** — the product provides the mechanism.

**M6 — Aggregate periodic close (v19 only).** Posts a period-level true-up between the stock valuation
account and a stock variation account, rather than a per-transaction cost entry.

**`FACT VERIFIED` — TC-28. It is configured to run for ZERO companies in the available estate.** The cron
domain is `inventory_period = 'daily'` — widened to include `'monthly'` only at month-end — **and**
`inventory_valuation != 'real_time'`.

| Archive | Companies | `inventory_period` | Matching the cron domain |
|---|---|---|---|
| `BK12MAY26` | 44 | **all `manual`** | **0** |
| `iEVING_0723` | 44 | 43 `manual`, 1 `monthly` — **and that one is the `real_time` company, which the domain excludes** | **0** |
| `iTEST02` ×2 | 1 each | `daily` — **but `real_time`, which the domain excludes** | **0** |

**And independently: `account_stock_journal_id` is NULL in 44 of 44 companies in both large archives**, so
even if the close were eligible there is no journal to post into.

**This strengthens TC-02 rather than weakening it.** The estate recognises no cost of sales through this
process by **any** mechanism — not transaction-level, and not aggregate.

### 15.2 §3.2 understated the change: v19 *redefines* what "perpetual" means

**`FACT VERIFIED` — TC-29.** The v19 valuation selection is not merely re-gated, it is **relabelled by the
product itself** (`EV-P02-113`):

```
('periodic',  'Periodic (at closing)')
('real_time', 'Perpetual (at invoicing)')        default = 'periodic'
```

against v18's `('manual_periodic','Manual')` / `('real_time','Automated')` on the product **category**.

**This is the single clearest statement of TC-09 available, and it comes from the product's own interface
label: in v19, "Perpetual" means "at invoicing".**

**`FACT VERIFIED` — TC-30 (AND IT BEARS DIRECTLY ON THE BOSS TARGET POLICY).** `23` §1 records **BP-02** —
*for a normal perpetual storable target, COGS is recognised at delivery*. On the v19 line **that policy is
not selectable**: choosing "Perpetual" selects *at invoicing*, by definition. BP-02 on v19 therefore
requires a mechanism the product does not offer, not a setting. This raises BP-02 from "a design
requirement with a known implementation gap" (`23` §1) to **a design requirement that the current product
generation contradicts by construction**.

### 15.3 Drop-shipping — v19 produces no cost entry anywhere in Order-to-Cash

**`FACT VERIFIED` — TC-31.** In v19 a dropshipped sale is excluded on **three** independent paths, verified:

1. **No stock-side entry** — the delivery gate requires `is_valued`, defined as `is_in or is_out`, and a
   dropship move is neither.
2. **No invoice cost line** — `_eligible_for_stock_account` ends `return all(not m._is_dropshipped() ...)`
   (`EV-P02-114`), so the line is skipped by the cost generator.
3. **No vendor-bill account redirect** — the same predicate gates the purchase-side substitution, so the
   bill keeps its ordinary expense account.

v18 had a **purpose-built** dropship entry for exactly this case. **The v19 O2C leg posts revenue and
receivable and nothing else**; cost recognition displaces entirely to the vendor bill, at the bill's date,
with nothing linking it to the sale. **Routed to P01**, which now owns cost recognition for dropshipped
sales on the v19 line.

### 15.4 A premise in this session's own research brief was wrong

**`CONTRADICTED` — TC-32.** The brief for the scenario track implied the period-end **unrealised FX
revaluation** fields might be v19-only. They are **present in v18 at identical definitions**
(`EV-P02-115`). The mechanism is **Enterprise-licensed in both generations**, so a Community-equivalent
deployment has never had it — which is the finding that matters, and it is not a generation change.

**Recorded as a research error of this session** (`RE-14`): a brief asserted a generation difference from
a field list rather than from a check, and the track corrected it. **The instruction in that brief to
report any wrong path as a finding is what surfaced it.**

### 15.5 A v19-only cost divergence for lot-valuated products

**`FACT VERIFIED` — TC-33.** In v19 the stock side values a move at the **lot's** standard price for every
cost method, while the invoice cost line uses the lot-derived value **only** for `fifo` or
`lot_valuated + average`. For **`lot_valuated + standard`** the invoice uses the **product's** standard
price. Where the two differ — which is the entire purpose of lot valuation — **the posted cost does not
equal the move's own recorded value**. v18's layer-backed design could not produce this, because both
sides read the same lot-tagged layers.

**Magnitude in the estate: `UNRESOLVED — EVIDENCE REQUIRED`** — it needs the count of products with
`lot_valuated` **and** `cost_method = 'standard'` **and** `valuation = 'real_time'`, which was not run.

### 15.6 Corrected mechanism inventory

| # | Mechanism | v18 | v19 | Deployed instances |
|---|---|---|---|---|
| M1 | Delivery-based (outflow posts cost) | present | **absent for ordinary sales** | **1** (`iSMEs`) |
| M2 | Invoice-based | gated on the company boolean | gated on **product valuation = real-time** | **0** |
| M3 | Valuation-layer-derived | present | **model does not exist** | 1 (v18 only) |
| M4 | Location-based | absent | present | **0** |
| M5 | Manual periodic (human posts an entry) | outside the process | outside the process | unmeasured |
| **M6** | **Automated aggregate periodic close** | **absent** | **present** — `EV-P02-111`, `EV-P02-112` | **0 — no company matches the cron domain** |

**`FACT VERIFIED` — TC-34.** Six mechanisms. **One has deployed instances, in one database.** Four have
zero. One is unmeasured and lies outside the process in both generations.
