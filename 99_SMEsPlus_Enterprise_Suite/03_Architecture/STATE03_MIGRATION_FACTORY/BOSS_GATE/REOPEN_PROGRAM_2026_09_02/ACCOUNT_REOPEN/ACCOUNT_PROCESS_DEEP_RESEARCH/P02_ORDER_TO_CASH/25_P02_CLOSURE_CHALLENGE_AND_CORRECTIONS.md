# 25 — P02 CLOSURE: INDEPENDENT CHALLENGE AND CORRECTIONS

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

`Independent Review != Truth. Verified Evidence = Truth Basis.`
**Every refutation below was independently re-derived by the primary session before acceptance.**

## 1. Outcome

A fresh four-expert AAS-03 panel was run against `22`. It produced **seven refutations of `FACT VERIFIED`
claims**, **one refuted claim in `13`**, **two new reference-ERP defects**, and **three new deployed-data
findings**. This is a worse result than the first challenge, which refuted two.

**What survived unchanged** — re-derived by the panel independently:

| Claim | Panel verdict |
|---|---|
| TC-02 — zero COGS lines in 448,017 journal lines | **reproduces exactly**, including the five marker values |
| TC-14 — the period mismatch exists and is large | **reproduces exactly**, and survived **four** alternative definitions |
| TC-16 — all eight outbound accounts are not reconcilable | **reproduces completely** |
| §3.2 — the four v19 structural changes | **all four verified independently** |
| TC-12's "no deployed instance" | **verified** — no location in any v19 archive carries a valuation account |

## 2. Refutations Accepted — Each Re-Derived By The Primary Session

### C-21 — `iSMEs` is Odoo **16.0**, not v18. A third generation is deployed, and it is the only database with transactions.

**Re-derived.** `ir_module_module` in that archive: `base 16.0.1.3`, `account 16.0.1.2`,
`stock 16.0.1.1`, `stock_account 16.0.1.1`, `sale_stock 16.0.1.0`, `l10n_th 16.0.2.0` — all `installed`.
The panel corroborated five further ways, including the **absence** of the picked-marker column that the
v18 valuation gate depends on.

**Consequences, all package-changing:**

1. `22` §3.1 describes a v18 mechanism that **no deployed database on this host runs**.
2. TC-11's *"M1 is the only mechanism observed operating"* attributes observed behaviour to the wrong
   generation.
3. `12` C-20's repair — *"read `01`–`11` as v18-scoped"* — is **the wrong repair**. The correct statement
   is stronger and worse: **the v18 analysis describes zero deployed instances in the available estate.**
4. **No Odoo 16 core source exists on this host.** So the mechanism that produced 56,772 posted valuation
   entries in the only database with volume **cannot be read from source at all**. That is an evidence-base
   gap the closure did not name.

**`SUPPORTED INTERPRETATION`.** The package now spans **three** generations — 16.0 deployed with volume,
19.0 deployed without volume, 18.0 read from source and deployed nowhere.

### C-22 — TC-01's archive denominator is refuted twice over

**Re-derived.** Two further deployed archives exist and were never opened:
`BK12MAY26_2026-08-03_11-28-04.zip` and `iEVING_2026-03-30_02-30-18.zip` — Odoo **web-backup ZIPs**
containing `dump.sql` plus `manifest.json`.

**`22`'s search pattern was `*.dump`, `dump.sql`, `*.backup` — it never looked inside archives.** This is
the **third** evidence-base failure in this package, after `RE-13` and the tooling gap, and it is the same
class: a negative claim resting on a pattern narrower than the claim.

**And the deduplication key was wrong.** `22` deduplicated by file content. The authoritative key is the
database UUID in each archive's own configuration table:

| Distinct database (by UUID) | Archive files | Generation |
|---|---|---|
| iSMEs | 1 | **16.0** |
| iTEST02 | 2 (same database, two dates) | 19.0 |
| iEVING *(uuid f4a4…)* | **1 — never examined** | 19.0 |
| iEVING *(uuid 1f63…)* | 2 (same database, two dates) | 19.0 |
| BK12MAY26 | 2 — **one never examined** | 19.0 |

**8 archive files. 5 distinct deployed databases. "6" is neither.**

**Neither newly-opened archive changes the zero-COGS conclusion** — the panel extracted both and found
0 COGS lines, no valuation-layer table, periodic valuation.

### C-23 — "93 company records" is a snapshot-sum over duplicate databases

Two pairs of archives are the **same database at two dates**, and both members of each pair were counted.
Counting the largest snapshot per database gives **91**; counting distinct legal entities by name gives
**≈46**. **Every "of 93" ratio in TC-02, TC-03, TC-06, TC-13 and TC-18 is over an inflated denominator.**

This is the `count-unit-vs-population` defect: the unit was declared ("company records") and then used as
though it meant "companies".

### C-24 — TC-03 is contradicted by TC-07, four lines below it

TC-03: *"`anglo_saxon_accounting` is **false in all 93 company records**"*. TC-07: company 28 carries
**NULL**. **NULL is not FALSE.** Correct: **false in 91, unset in 2.**

**This is the third occurrence of the same failure mode in this package** — after C-19 (`P02-F-43`
refuted by evidence two sections below it) and the first challenge's CH-15. A claim and its refutation
sitting in the same file, four lines apart, survived authorship and self-review.

### C-25 — TC-04's periodic count does not close

The table cell reads **88**; the prose beside it sums to **89** (44 + 43 + 2). Re-derived: **89** is
correct. `totals-are-unverified-claims`, again, in the same package that recorded that lesson.

### C-26 — TC-08 is false for two of the three real-time companies

Both `iTEST02` real-time companies **do** carry `account_stock_journal_id = 8`. TC-08's conclusion
collapses to one company.

**The sound version is the inverse, and it is worse:** all **89 periodic** company records have a NULL
stock journal, and the closing routine **raises** for want of one. **The mechanism the periodic majority
depends on cannot run.**

### C-27 — TC-15's direction REVERSES on the accounting date. **This is the most consequential correction.**

`22` §6 measured the cost month from the **movement's** date. The date that determines the accounting
period is the **posted valuation entry's** date. Re-derived by the primary session:

| Measure | Movement date (published) | **Posted valuation entry date** |
|---|---|---|
| Population | 3,880 | 3,865 |
| Cost month = revenue month | 2,152 — 55.5% | **2,642 — 68.4%** |
| **Mismatch** | 1,728 — **44.5%** | **1,223 — 31.6%** |
| Invoice **before** cost | **1,355** | **516** |
| Cost **before** invoice | 373 | **707** |

**TC-14 survives — the mismatch is real and large at 31.6%.** **TC-15 does not** — it claimed the
mismatch is *predominantly invoice-before-delivery* and that *revenue is recognised before its cost in more
than a third of all matched order lines*. On the correct date the ordering **flips**, and revenue-before-cost
falls from 34.9% to **13.3%**.

**And the caveat that permitted the error was itself false.** `22` §6 stated the movement date *"in this
generation equals its validation date"*. The panel found **10,871 counter-examples** out of 56,444 linked
layers — 19.3% differ by month.

**`22` §6's own sentence — *"Neither choice can move a 44.5% result to a small one, but both are
choices"* — is true of the magnitude and false of the finding that carries the accounting consequence.**

### C-28 — §12's cash-basis conclusion is refuted by 7,738 posted entries

`22` §12 concluded *"no tax is actually treated on a cash basis"*. In `iSMEs`: one tax is set to
on-payment exigibility (`Undue VAT 7%`, **purchase**-side), and the cash-basis journal holds **7,738
posted entries**.

**Corrected statement, and this is what P07 must receive:** deployed per-tax exigibility **is** set, on
the **purchase** side only, so cash-basis treatment **runs at scale** but does not reach the P02 sales
side. As published, §12 handed P07 a refuted conclusion.

## 3. New Reference-ERP Defects Found By The Panel

### D-01 — The v19 periodic-close cron domain is unsatisfiable at month-end

**Re-derived from source.** The domain is built as
`[('inventory_period','=','daily'), ('inventory_valuation','!=','real_time')]`, and at month-end it is
combined with `('inventory_period','=','monthly')` using **`&`**, not `|`.

**Result: `inventory_period = 'daily' AND inventory_period = 'monthly'` — which nothing satisfies.**

- A company set to `monthly` **never** gets an automatic close.
- On the last day of every month, even `daily` companies are skipped.

**`13` `EV-P02-112` read this as *"widened to `'monthly'` at month-end"*. That reading was wrong** and is
corrected here. **This is a defect in the reference product**, filed with its three-line citation.

### D-02 — In v19, an invoice can relieve inventory for goods that never moved

The cost-eligibility test ends `return all(not m._is_dropshipped() for m in moves)`. **`all()` over an
empty recordset is `True`**, and the base movement getter returns an empty recordset. The cost-value
helper handles the no-move case explicitly, falling back to standard price or a synthetic consumption.

**So posting a customer invoice for a storable, real-time product with no delivery at all creates
`Dr Expense / Cr Inventory`.** Combined with C-27's data — this deployment invoices before shipping on
1,089 order lines in a single month-offset bucket — **this is not a theoretical path.**

## 4. New Deployed-Data Findings

### F-01 — 30 posted journal entries are dated in the Buddhist Era

In `iSMEs`, `account_move.date` carries **30 rows in year 2567** — Thai Buddhist Era leaked into a
Gregorian field — all **posted**, all in the **cash-basis tax** journal, carrying 120 journal lines. The
movement table shows the same class: 6 moves dated `8202`, three of them completed.

**This company has no lock date of any kind**, so these are permanent and re-datable. **Routed to P07 and
P08.**

### F-02 — The "expense" accounts are shared with manufacturing

The eight outbound accounts are used **two-sided at scale** inside the inventory-valuation journal — one
carries credits of 4.13bn against debits of 7.23bn; another carries **credits larger than its debits**.
Counterparties are raw material, work in progress, finished goods and the goods-receipt-note account.

**These accounts carry the manufacturing flow, not cost of sales.** Any statement that this deployment
"recognises cost of sales at delivery, directly to an expense account" must add *and also runs its entire
manufacturing consumption through the same accounts*. **The corroborating 0.42–1.33 ratio in `22` §6 is
measured over contaminated accounts and is withdrawn as corroboration.**

### F-03 — The three-outcome model is a per-category choice with a silent default, not a per-company one

Within `iSMEs`, the **global default is manual/periodic** and 15 of 30 categories carry an explicit
real-time override — and the overrides do **not** follow the category tree: two sales-revenue categories
are real-time while their **parent** saleable-goods categories are not.

**So within one legal entity, some sales relieve inventory at delivery and others never do**, decided by a
property on a category, silently inherited from a global default that recognises no cost at all.
`21` §4.2 presented this as a per-company choice. **It is a materially weaker control than described.**

## 5. Corrections The Panel Made To Its Own Framing — Accepted

| Panel finding | Accepted correction |
|---|---|
| M4 "Location-based" is mislabelled | The location valuation account is exposed in the interface **only** for inventory-loss and production locations. It is the scrap/production mechanism, **not** an alternative O2C cost route. |
| TC-12 is half the collision, and the reachable half points the other way | The **source**-location branch takes precedence. An internal source location with a valuation account makes an outbound delivery **increase** inventory. And reaching it on a customer location requires bypassing the form view — so *"reachable by ordinary configuration"* overstates it. |
| TC-09's framing overstates novelty | The inversion is stated by v19 **in its own interface labels**, which `13` `EV-P02-113` already recorded. The finding is sound; presenting it as a discovery is not. |
| `22` §3.3 is stale against `13` | The mechanism inventory omitted M6 while the evidence register already held it. **A headline deliverable stale against its own register.** |

## 6. What The Panel Could Not Check

Recorded because it bounds this challenge exactly as the last one was bounded:

1. **The Odoo 16.0 mechanism** — no 16.0 source on this host. Everything about *how* `iSMEs` generated its
   entries is inference from posted data.
2. **Runtime** — nothing executed, by the closure or the panel. D-01, D-02 and the TC-12 re-scope are
   source-read, not runtime-confirmed.
3. **The two newly-opened archives** were examined only for the dimensions in dispute.
4. **Sub-month cut-off** — everything is at month granularity.
5. **Custom addons** — the panel searched only the two declared reference roots. **It states plainly that
   it has not established that those roots are the code these databases run.** A custom override could
   change any code-path conclusion.

**Point 5 compounds `23` §7 item 5:** P02 has examined **no custom module**, and two peer processes found
their highest-severity findings in custom modules.

## 7. Method Record

| Round | Refuted `FACT VERIFIED` claims | New defects | New gaps |
|---|---|---|---|
| Self-review (rounds 1–2) | 6 corrections, 0 refutations | — | — |
| First independent challenge | **2** | — | 6 |
| Peer process (P06) | **1** | — | — |
| **This challenge** | **7 + 1 in the register** | **2** | 3 |

**The rate of refutation went up, not down, in a round explicitly commissioned to close the package.**
That is the single most important fact for the exit assessment, and it is why `EC-02` and `EC-07` cannot
move.

**The recurring failure is not in the evidence — it is in aggregation and in scoping:** a generation
inferred rather than checked, a denominator built on the wrong key, a total that does not sum, a claim
contradicted four lines below itself, and a date field chosen by convenience and then caveated instead of
tested.
