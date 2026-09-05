# 25 — P05 RUNTIME / DATABASE TRACE (`U-02`)

`LAYER 2 — AUDIT QUARANTINE`

## 1. What Was and Was Not Obtained

| Evidence class | Status |
|---|---|
| **Database evidence** (persisted state of real deployments, read offline) | **OBTAINED** — substantial, production scale |
| **Runtime evidence** (a live instance executing P05 code paths under observation) | **NOT OBTAINED** |

Runtime execution would require standing up an instance and installing modules — a write and deploy
action prohibited by the continuation directive §3.13. `READ-ONLY FIRST` was honoured: every byte
below was read from dump files with `pg_restore -f`, never with `-d`.

> **`U-02` is therefore split.** The half that database evidence can answer is **closed**. The half
> that requires observing code execute is **HOLD — RUNTIME EVIDENCE REQUIRED**, and the specific
> authorisation needed is named in §6.

## 2. Population Read

From `iSMEs` (v16, owner `scgl`) — the only registry with production-scale P05 data:

| Table | Rows |
|---|---|
| `account_move` | **183,590** |
| `withholding_tax_cert` | **5,201** |
| `withholding_tax_cert_line` | **6,159** |
| `account_withholding_tax` (configuration) | 7 |
| `purchase_advance_payment_bill` | 21 |
| `hr_expense` | 2 |
| `hr_expense_sheet` | 0 |

`account_move` composition: `entry` 143,811 · `in_invoice` 37,055 · `out_invoice` 2,602 ·
`in_refund` 116 · `out_refund` 6. States: `posted` 169,143 · `draft` 12,581 · `cancel` 1,866.
Moves carrying a non-zero `wht_amount`: **1,186**.

## 3. Findings Empirically Tested

> ## CORRECTION NOTICE — read before §3
>
> **Two of the three findings originally published in this section were wrong, and both were
> corrected by independent review (AAS-03 Expert 2, Leadership Database Design), not by the author.**
> Every one of Expert 2's counter-measurements was then independently re-run by the author against
> the same data and **reproduced exactly** — per the standing rule that a reviewer's disproof must
> itself be verified before adoption. The original claims are preserved below, struck through, with
> the corrected finding beside them. See `39 RE-10`..`RE-13`.

### `TX-13` — duplicate withholding certificates — **ORIGINAL CLAIM OVERSTATED ~30×**

~~*"32 payments hold multiple live statutory certificates with no substitution link between them."*~~
**WITHDRAWN as written.** The 32 is arithmetically right and materially misleading. Decomposed:

| Group | Payments | Verdict |
|---|---|---|
| Certificates carrying a `payment_id` | 3,794 across 3,710 distinct payments | — |
| Payments with >1 certificate (any state) | **32** | the original headline |
| — of those, **one certificate per distinct supplier** | **21** | **LEGITIMATE.** These are bulk payment runs: payment 21525 (THB 15,719,556.92) and 21873 (THB 35,692,904.01) each carry 9 certificates naming 9 **different** suppliers. A withholding certificate is issued per payee; N payees on one payment requires N certificates. |
| — >1 certificate for the **same** supplier | 11 | candidates |
| —— of those, done + draft pairs | **2** | not two live certificates |
| —— of those, same supplier at **different withholding rates** (1% and 3%) | **8** | legitimate content; arguably belongs on one certificate as two lines — the schema supports that and 424 certificates already do it — but not a duplicate document |
| —— **genuine exact duplicates** | **1** | payment 659, certificates 124 and 126: same supplier, **identical certificate number `JRCSH12023100176`**, identical single line (base 1800, 1%, tax 18, same `ref_move_line_id`), created 30 and 31 Oct 2023 |

**Defensible restatement, author-verified:** *one exact duplicate certificate in a population of
5,201*, plus 8 rate-split pairs and 2 draft residues. Restricted to state `done`, the payment count
falls from 32 to **30**, and the same-payee groups to **11**.

The author's own filter caused the overstatement: it used `state != 'cancel'`, which admits `draft`,
and it never grouped by supplier. Class: **FACT VERIFIED** for the corrected figure; the original
figure is class **E — CONTRADICTED**.

**What survives, and it is the load-bearing half.** The structural claim is confirmed at schema level
from the *unfiltered* schema: `withholding_tax_cert` carries **no UNIQUE constraint and no index of
any kind beyond `withholding_tax_cert_pkey PRIMARY KEY (id)`** — in the v16 registry and in all three
v19 registries. Nothing at any layer prevents a duplicate certificate; the one that exists proves the
gap is reachable, and the control remains a client-side domain the creation wizard bypasses via
context. **`TX-13` stands as a control defect with one production instance, not as a mass-duplication
finding.**

### `TX-20` — certificate dating — **ORIGINAL CLAIM INVERTED**

~~*"4,081 of 5,201 certificates — 78.5% — carry a date that is not the payment date"*~~ —
~~attributed to `date` being set from a create-time default.~~ **CONTRADICTED. The mechanism is on the
other column, and the sign is reversed.**

The author compared `date` against `payment_date` and assumed `payment_date` was the truth. It is not.
Joining to the **actual** payment date (`account_payment.move_id` → `account_move.date`; 3,794
certificates joined, **0 unjoinable**):

| Measurement | Result |
|---|---|
| `payment_date` == `create_date::date` | **5,201 of 5,201 — 100.00%, zero exceptions** |
| `cert.date` == the real payment date | **3,710 of 3,794 — 97.79%** |
| `cert.payment_date` == the real payment date | **609 of 3,794 — 16.05%** |
| `payment_date` − real payment date, top deltas | −1: 1,394 · −2: 954 · **0: 609** · −3: 411 · −4: 103 · −7: 39 |

**The field printed on the statutory certificate — `date` — is correct in 97.8% of cases.** The
create-time artefact sits on `payment_date`, and the deltas are **negative**: certificates are created
*before* the payment is dated, which is the opposite of the drift the author reported.

**The corrected finding is arguably worse than the original, and is retained on that basis:**
a column named `payment_date`, declared `NOT NULL`, **carries no payment information in 100% of rows**
— it is a record of when the certificate was keyed. Any downstream consumer that reads `payment_date`
as the payment's date is wrong 84% of the time. Class: **FACT VERIFIED** (`iSMEs` v16).

### `TX-15` — unreportable certificate forms — **CONFIRMED**

`pnd53` 4,437 · `pnd3` 751 · **`pnd1` 13**, all `done`, 12 with a `payment_id`, one unlinked and
unnamed. The report wizard offers only `pnd3`/`pnd53`, so those 13 cannot be exported by either path.
Independently reproduced by Expert 2. Class: **FACT VERIFIED** (`iSMEs` v16).

### `TX-10` — inverted receipt move types — **NOT EXERCISED**

`in_receipt`/`out_receipt` moves in the population: **0**. The source defect stands (`11 C-02`,
settled against four core authorities). No operational footprint in this database: **latent, not live**.

### `TX-14` — substitution chain — **HELD AT CLASS D, with a third explanation added**

Only 6 of 5,201 certificates carry `ref_wt_cert_id`. Expert 2 supplied an explanation the author had
not considered: `withholding_tax_cert_ref_wt_cert_id_fkey` is **`ON DELETE SET NULL`**, so deleting a
predecessor silently erases the link. Sparse population is therefore consistent with recompute
clearing, with substitution being rare, **and** with FK-driven silent erasure. Class **D** was the
right call; the reasoning published for it was incomplete.

### Population caveats the author omitted

| Fact | Value |
|---|---|
| Certificates with **neither** `payment_id` nor `move_id` | **1,407 (27.1%)** |
| Certificates with `move_id` populated | **0** — every certificate is payment-based |
| Certificates with a **NULL `name`** (no certificate number) | **1,417**, of which **1,414 are state `done`** |
| Certificate numbers shared by more than one certificate | **75** |
| Certificate lines orphaned (`cert_id IS NULL`) | **362 of 6,159 (5.9%)** |

`TX-20`'s denominator therefore included 1,407 rows for which "the payment date" is undefined.
Restricted to payment-linked rows the original divergence figure would have been 83.26%.

## 4. Version Boundary — read before relying on §3

The empirical results come from a **v16.0** database running `l10n_th_withholding_tax 16.0.1.0.1`.
The source analysis was against the **v18** custom copy (`18.0.1.4`).

| Statement | Class |
|---|---|
| The corrected `TX-13` and `TX-20` figures for `iSMEs` v16 | **A — FACT VERIFIED** in that database |
| No UNIQUE constraint or index on `withholding_tax_cert` in v16 **or** any of the three v19 registries | **A** within those four schemas |
| The same holds at v18 | **D — UNKNOWN.** v16 and v19 bracket it, but no v18 population exists. **Not upgraded.** |

**A denominator defect in the author's own version reasoning, found by Expert 2 and confirmed:** the
original text said *"`iTEST02` (v19) holds 0 certificates and `iEVING` holds 0, so no v19 population
exists to measure."* That enumeration was author-chosen rather than driven by the registry set the
package had already declared — it omitted `BK12MAY26`, listed as v19 registry `R-d` in `24 §2` with
the certificate module installed. **`BK12MAY26` holds 1 certificate and 1 line.** The claim "no v19
population exists" is class **E — CONTRADICTED** by a root inside the package's own declared path set.
That is the second time in this package a negative has been contradicted by its own declared roots
(the first was `21 NC-E-05`).

**A structural change between v16 and v19 further weakens the bracketing argument**, and it is
recorded rather than glossed: at v19 `withholding_tax_cert_line` gains its own `payment_id` and
`move_id` foreign keys, so payment linkage moves to line level — which changes what "one certificate
per payment" even means at the target version. v19 also adds `amount_pension_fund`,
`amount_socialsecurity_fund` and `amount_provident_fund`, i.e. PND1 payroll support, bearing directly
on `TX-15`'s reportability claim at the target version.

## 4b. Database-Design Findings (raised by AAS-03 Expert 2, author-verified)

None of these were in the author's package. All are from the **unfiltered** schema and the data.

| ID | Finding | Evidence | Class |
|---|---|---|---|
| `DB-01` | **No UNIQUE constraint on `payment_id`** — and no unique constraint of any kind beyond the primary key — in the v16 registry and all three v19 registries. This is the schema-level half of `TX-13`. | only `withholding_tax_cert_pkey PRIMARY KEY (id)` | **A** within four schemas |
| `DB-02` | **No index at all** on `withholding_tax_cert` beyond its primary key. `payment_id`, `move_id`, `supplier_partner_id`, `name`, `date` are all unindexed. The only index in the subsystem is `withholding_tax_cert_line_cert_id_index`. Every payment→certificate lookup is a sequential scan. | unfiltered schema, four registries | **A** |
| `DB-03` | **`withholding_tax_cert_line.cert_id` is nullable with `ON DELETE SET NULL`** — deleting a certificate **orphans** its statutory lines instead of removing them. **362 of 6,159 lines (5.9%) are already orphaned.** | FK definition + data | **A** |
| `DB-04` | **No uniqueness on `name`.** 75 certificate numbers are shared by more than one certificate, and **1,417 certificates have no number at all** (1,414 of them `done`). A statutory document identifier is neither unique nor mandatory. | data | **A** |
| `DB-05` | `cert.supplier_partner_id` disagrees with `account_payment.partner_id` on **1,031 of 3,794** payment-linked certificates (27.2%), including 940 of 3,678 **singleton** payments — so batch payments do not explain it. Cause not established. | join | **A** (fact) / **D** (cause) |
| `DB-06` | **v16 → v19 statutory-column regression.** v16 declares `date`, `income_tax_form` and `supplier_partner_id` `NOT NULL`; **v19 makes all three nullable** while `payment_date` stays `NOT NULL`. The single v19 row already exercises it — NULL `income_tax_form`, NULL `supplier_partner_id`. The database now permits a withholding certificate with no payee and no tax form. | schema diff | **A** |
| `DB-07` | v19 moves payment linkage to line level and adds PND1 payroll fields — see `§4`. | schema diff | **A** |
| `DB-08` | `account_payment.wt_cert_cancel` is `f` on 3,706 payments while 3,710 actually carry a certificate — 4 payments where the derived flag disagrees with reality. | join | **A** |
| `DB-09` | Two certificates have **zero** lines; one has 17. `base`, `wt_percent` and `amount` are all nullable, and certificate 3133 carries `base=0, wt_percent=0, amount=72` — an arithmetically impossible line the schema accepts. | data | **A** |

> **Method defect found in the author's own work, and worth propagating.** `pg_restore -s -t <table>`
> returns **only** the `CREATE TABLE` — **zero** constraint, index or FK lines — because those are
> separately-named archive objects the `-t` filter excludes. Verified: the filtered extract yields 0
> matches for `CONSTRAINT|CREATE INDEX`; the unfiltered schema yields the full set above. **Any
> "no constraint exists" conclusion drawn from `-s -t` is a false negative.** The author used `-s -t`
> when reading the certificate schema. Recorded as `39 RE-13`.

## 5. Trace Table — where each stage could be evidenced

| Stage | Source | Database | Runtime |
|---|---|---|---|
| Expense claim capture → sheet → approval | ✔ | ✗ (2 expense rows, 0 sheets) | ✗ |
| Company-paid per-line payment creation | ✔ | ✗ | ✗ |
| Employee advance disbursement → liquidation | ✔ | **n/a — module installed nowhere** | ✗ |
| Petty cash float → spend | ✔ | **n/a — module installed nowhere** | ✗ |
| Vendor expense → bill → payment | ✔ | ✔ 37,055 vendor bills | ✗ |
| WHT configuration | ✔ | ✔ 7 codes | ✗ |
| WHT withheld at settlement | ✔ | ✔ 1,186 moves with `wht_amount` | ✗ |
| WHT certificate issue | ✔ | ✔ **5,201** | ✗ |
| WHT reporting / export | ✔ | ✔ (13 unreportable) | ✗ |
| Reconciliation | ✔ | partial | ✗ |
| Analytic distribution | ✔ | not extracted | ✗ |
| Period close | ✔ | ✗ | ✗ |

## 6. Disposition

| Aspect | Disposition |
|---|---|
| Database evidence for the WHT and vendor-expense chain | **CLOSED — EVIDENCE VERIFIED**, after two published findings were contradicted and corrected by independent review (§3) |
| Database evidence for the claim, petty-cash and advance chains | **CLOSED AS UNOBTAINABLE** — the modules are installed nowhere and the tables do not exist |
| Runtime (execution) evidence | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `U-02` overall | **PARTIALLY RESOLVED** |

**Specific authorisation that would close the residue:** permission to restore one of the existing
dumps into a disposable local database and run read-only ORM queries against it — or, better, an
Odoo 18 instance carrying the P05 custom modules. Both are write actions on infrastructure and were
**not** performed. `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` is recorded rather than assumed.
