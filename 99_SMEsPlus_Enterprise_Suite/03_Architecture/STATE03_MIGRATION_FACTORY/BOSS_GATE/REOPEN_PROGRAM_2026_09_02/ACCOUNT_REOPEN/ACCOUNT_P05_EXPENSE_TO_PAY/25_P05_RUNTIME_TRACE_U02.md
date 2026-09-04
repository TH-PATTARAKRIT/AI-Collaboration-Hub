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

### `TX-13` — duplicate withholding certificates — **CONFIRMED IN PRODUCTION**

Source claim: the "one certificate per payment" control is a client-side Many2one `domain`, and the
creation wizard sets the value through context, bypassing it. No constraint exists.

| Measurement | Result |
|---|---|
| Certificates carrying a `payment_id` | 3,794 across 3,710 distinct payments |
| Payments carrying **more than one** certificate | **32** |
| Payments carrying more than one **non-cancelled** certificate | **32** |
| Maximum certificates on a single payment | **9** |
| Certificates in state `cancel` | 5 of 5,201 |
| Certificates carrying a substitution reference (`ref_wt_cert_id`) | **6** of 5,201 |

The duplicates are not cancel-and-reissue chains: only five certificates are cancelled in the entire
population and only six carry a substitution reference. **32 payments hold multiple live statutory
certificates with no substitution link between them.** Class: **FACT VERIFIED** for this database.

### `TX-20` — certificate dated other than the payment — **CONFIRMED, AND WORSE THAN CLAIMED**

Source claim: `payment_date` is a local addition defaulting to `context_today`, and the certificate
`date` is set from it — so the certificate is dated when it was created, not when the payment occurred.

| `date` − `payment_date` | Certificates |
|---|---|
| **0 days (agree)** | **1,120** |
| +1 day | 1,746 |
| +2 days | 1,243 |
| +3 days | 532 |
| +4 days | 151 |
| +7 days | 40 |
| other | remainder |

**4,081 of 5,201 certificates — 78.5% — carry a date that is not the payment date**, and the
distribution is the signature of a create-time default, not of a business rule. Class:
**FACT VERIFIED** for this database.

### `TX-15` — unreportable certificate forms — **CONFIRMED WITH A COUNT**

The report wizard offers only `pnd3` and `pnd53`. The population contains `pnd53` 4,437, `pnd3` 751
and **`pnd1` 13**. Those **13 certificates cannot be exported** through either report path, and
`format_pnd` would raise on them. Class: **FACT VERIFIED** for this database.

### `TX-10` — inverted receipt move types — **NOT EXERCISED**

`in_receipt` and `out_receipt` moves in the population: **0**. The source defect stands
(`11 C-02`, settled by Expert 4 against four core authorities), but it has **no operational
footprint in this database**. Severity for the estate: latent, not live.

### `TX-14` — compute side-effects clearing the substitution chain — **CONSISTENT, NOT PROVEN**

Only 6 of 5,201 certificates carry `ref_wt_cert_id`. That is *consistent with* a recompute clearing
the field, and equally consistent with substitution simply being rare. **Class D — UNKNOWN.**
Distinguishing the two requires observing a recompute, i.e. runtime. **Not upgraded.**

### Petty cash and employee advance — **NO DATA EXISTS TO TEST**

`petty_cash` and `advance_expense_request` tables are absent from every dump. Consistent with `24 §3`.

## 4. Version Boundary — read before relying on §3

The empirical results come from a **v16.0** database running `l10n_th_withholding_tax 16.0.1.0.1`.
The source analysis was against the **v18** custom copy (`18.0.1.4`). These are different module
versions.

What can and cannot be carried across:

| Statement | Class |
|---|---|
| "In `iSMEs` v16, 32 payments carry multiple live certificates and 78.5% are misdated." | **A — FACT VERIFIED** in that database |
| "The `payment_date` field and its `context_today` default exist at v19 too." | **A** — confirmed from the v19 `withholding_tax_cert` schema, which carries `payment_date` |
| "The same defect is present in the v18 target." | **SUPPORTED INTERPRETATION.** The mechanism identified in v18 source produces exactly the pattern observed at v16, and the field survives to v19 — so v18 is *bracketed* on both sides. That is strong corroboration, **not** proof. **Not upgraded to FACT VERIFIED.** |

A v19 test was attempted for independent confirmation: `iTEST02` (v19) holds **0** certificates and
`iEVING` holds 0, so no v19 population exists to measure. Reported rather than omitted.

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
| Database evidence for the WHT and vendor-expense chain | **CLOSED — EVIDENCE VERIFIED** |
| Database evidence for the claim, petty-cash and advance chains | **CLOSED AS UNOBTAINABLE** — the modules are installed nowhere and the tables do not exist |
| Runtime (execution) evidence | **HOLD — RUNTIME EVIDENCE REQUIRED** |
| `U-02` overall | **PARTIALLY RESOLVED** |

**Specific authorisation that would close the residue:** permission to restore one of the existing
dumps into a disposable local database and run read-only ORM queries against it — or, better, an
Odoo 18 instance carrying the P05 custom modules. Both are write actions on infrastructure and were
**not** performed. `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` is recorded rather than assumed.
