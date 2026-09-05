# P01 — SERIES-16 AAS-03 FOUR-EXPERT CHALLENGE

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-11`

Four experts challenged a frozen brief. **Experts provide perspectives, not verdicts.** No expert issued a
binary verdict word. **Disagreement between them is preserved, not merged.** Every correction adopted below
was **re-derived in this package before acceptance**; those not re-derived are marked and carried with
attribution.

---

## 1. WHAT ALL FOUR REPRODUCED

All four independently reproduced the load-bearing arithmetic **to the digit**: the 4-cell policy/linkage
table (56,654 / 1,044 / 1,209 / 16,075) with coverage control 0 of 74,982; 10,490 PO lines; 79 received-not-
invoiced at ฿12,678,776.50; account 39 at 13,736 items; 6,653 bill lines at ฿4,516,394,611.47; 74,982 layers
with 57,863 linked; the 30 extreme layers and ฿400,338,755.98; residuals 296 and 1,209; ฿31,622,699.37.

> **Not one defect any expert found was an arithmetic error. Every one was a predicate, a population, or an
> interpretation.** The counts were right and the sets they were counted over were not declared.

---

## 2. THE CORRECTIONS ADOPTED, EACH RE-DERIVED HERE

| # | Published claim | Correction | Verified |
|---|---|---|---|
| A | GRN net **฿72,097,814.25** outstanding | **All-states figure.** Posted-only **−฿7,048,692.08** — opposite sign. 53 cancelled + 17 draft items carry it; one cancelled entry is ฿90,351,213.15 | **yes** — `ERR-P01-45` |
| B | *"The price-difference engine has never fired"* | **1,123 layers carry ฿2,246,313,274.64** of `price_diff_value` | **yes** — `ERR-P01-46` |
| C | Residual B = 1,209 policy violations | **Bill-created price-difference layers**; 1,194 have no stock move | **yes** — `ERR-P01-47` |
| D | Residual A = 296 anomalies | **245 are `product.type = 'consu'`**, skipped before any policy test | via experts 1 + 4 |
| E | *"Policy change refuted by time distribution"* | **The change happened.** `ir_property` cannot see history | via experts 1 + 4, two independent routes |
| F | BE dates: 30 in one column | **Far wider** — extent disputed, §4 | **yes** as to "wider" |
| G | Max `unit_cost` ฿744bn | **฿52,616,504,567,828,624** — understated ~70,713× | **yes** |
| H | Cost explosion originates in manufacturing → **P03** | **Originates in `purchase_stock/_get_price_unit` → P01's own path** | **yes**, source read line by line |
| I | *"The general ledger is intact and sane"* | **Broken.** §3 | **yes** |
| J | 6:1 bill-to-PO ratio | **73.1% non-PO by count, but 89.8% PO-linked by value** — unit never stated | via expert 1 |

---

## 3. THE CLAIM OF MINE THAT BROKE LAST, AND WHY IT BROKE

I published: *"The general ledger is intact and sane. The inventory subledger is not."*

**AAS-03 Expert 4 pointed out that I tested it only on the 25 journal entries reachable from the 30 extreme
valuation layers** — a population selected **from the subledger side** to answer a question **about the ledger**.

Queried from the ledger side instead — `account_move_line` with `|debit|` or `|credit|` > 1e9, posted only:

| Move | Date | Amount |
|---|---|---|
| `STJ2023110741` | 2023-11-23 | **Cr ฿19,784,867,370.00** |
| `STJ2023110750` | 2023-11-23 | Dr ฿19,745,654,299.40 |
| `STJ2024092277` | 2024-09-30 | Cr ฿1,740,218,267.76 |

**8 posted journal items exceed ฿1 billion.** The first two are a posting and its partial revaluation
reversal, leaving **≈฿39.2m misallocated between Work in Progress and Semi Product** — a real, posted,
unreversed GL effect.

> **The claim is withdrawn.** The correct statement is: *the subledger and the ledger diverge by ~10¹⁵ on the
> 30 layers examined, **and** the ledger separately carries at least 8 posted items above ฿1bn, of which one
> pair leaves ฿39.2m misallocated.*

**The defect class is the one this package has been caught by repeatedly** — the population was chosen by
what I had already found rather than by the subject of the claim.

---

## 4. WHERE THE EXPERTS DISAGREE — PRESERVED, NOT RECONCILED

### 4.1 Why account 1173 is empty

| Expert 2 | Expert 1 |
|---|---|
| **Six product-level overrides** route the price difference to six other accounts, one named `9999991 Dummy Service`, the most recent configured 4 days before the archive | **Correct-by-construction behind two independent gates**: `purchase_stock/models/account_invoice.py:35` returns early because `anglo_saxon_accounting = FALSE`, and `purchase_price_diff` routes to 1173 only for `cost_method == 'standard'` while the one configured category is `fifo` |

Both agree the ฿2.25bn is real and my published conclusion was wrong. **Neither mechanism is adopted.**
Expert 1's cites two gates and is the stronger on its face; **neither was re-derived here.**

### 4.2 The extent of Buddhist-era leakage

| Expert 2 | Expert 4 |
|---|---|
| **484 values across 14 columns in 11 tables**, plus 11 at year 8202 (a second, undiagnosed class); bidirectional | **12 (table, column) pairs across 7 tables** — 120 posted journal items and 120 analytic lines |

**Both far exceed the 30 I published; they do not agree with each other.** The lower bound common to both is
adopted — *"materially wider than 30 rows in one column, and no date column is reliably Gregorian"* — and the
exact extent is `UNRESOLVED — EVIDENCE REQUIRED`.

**Expert 4 additionally establishes the mechanism**, which Expert 2 did not test: the dates are **typed, not
converted**. No installed module writes or converts dates (`scgl_tax_period_date` is 45 lines and
date-neutral; every `+543` lives in a report layer). `th_TH` is active with `%d/%m/%Y`, **all 178 BE picking
dates end `17:00:00`** — midnight Bangkok expressed in UTC — and correct CE `create_date`s sit beside them.
Expert 1 independently establishes that the 30 `account_move` cases are **cash-basis VAT entries derived from
posted vendor bills**, i.e. they originate in the P2P chain.

### 4.3 Certificate/payment gap counts

Expert 3: 1,407 certificates with no payment link; 1,543 of 5,232 WHT-bearing payments with no certificate.
Expert 1: 1,405 done certificates with no payment link; 1,488 withheld payments with no certificate.
**Different denominators (`done` vs all; `payments` vs `items`).** Both are recorded; neither is averaged.

---

## 5. THE FINDING THAT REACHES BACK ACROSS THE PROGRAMME

**AAS-03 Expert 4, verified here directly from the schema:**

```
stock_valuation_layer_account_move_id_fkey FOREIGN KEY (account_move_id)
    REFERENCES public.account_move(id) ON DELETE SET NULL;
```

*Positive control: the schema contains 584 `ON DELETE CASCADE` and 1,741 `ON DELETE SET NULL` clauses, so the
query discriminates.*

And `om_data_remove` — **installed here at 16.0.1.0.1** — executes raw `DELETE FROM <table>` followed by
`commit()`: **no ORM, no lock-date check, no company filter, no log**, and 10 of its 20 destructive buttons
carry no confirmation.

> ### Therefore a raw deletion of journal entries silently sets `account_move_id` to NULL on every valuation
> ### layer that referenced them — reproducing **exactly** the *"0 of N valuation layers linked"* signature
> ### that P01 published for the series-18 OCC deployment (0 of 47,801) and the series-19 estate (0 of 14,441).

**This does not overturn those findings.** For series 18 the periodic policy was proved positively and
independently — 126 of 126 categories, both storage locations read, with the source gate closed. That
explanation stands on its own evidence.

**What it does is introduce a competing hypothesis that was never excluded**, and the programme has been
reading those zeros as *"never posted"* when *"posted and later deleted"* would look identical.

**Expert 4 found no evidence the module ran in this deployment** — every target table is populated with low
minimum ids — **and states the limit of that test**: two target tables are empty, and the module leaves no
trace by design.

**Registered as blocker `S16-B-05`, routed to P11 and P06, and it must be tested in the series-18 and
series-19 deployments before either zero is relied on again.**

---

## 6. WHAT ELSE THE EXPERTS ADDED THAT THE PACKAGE DID NOT CARRY

| Item | Source |
|---|---|
| The deployment's custom source is **one directory**, `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons` — **45 of 46** deployed non-core modules, 43 exact-version, 2 one patch *ahead* | Expert 4 |
| **7 writers** of `stock_valuation_layer.account_move_id` in installed core, **0 in custom code** (with a positive control). The 7th, `_prepare_in_invoice_svl_vals`, has **no valuation predicate at all** | Expert 4 |
| **Version strings do not identify this code**: 4 `_cert` variants share one, 6 `_report` variants share another; one on-disk copy is uncommitted 246 lines ahead. **Discriminate on the deployment's `ir_model_fields` registry** | Expert 3 |
| **A rate record named `WHT3%` carries the value 0** — most-used rate, 2,038 payments; ฿21,556,228.06 posted after it was zeroed; amounts are hand-entered via a payment write-off | Expert 3, verified here |
| The submission file hardcodes income code "2" (99.81% mismatch), mixes Gregorian and BE year fields, and **cannot select the 13 `pnd1` certificates at all** | Expert 3 |
| **Account 39 has `reconcile = 'f'`** — no item-level matching; 39 manual `MISC` items sweep ฿1.9bn out of it | Expert 1 |
| ฿14,429,800.46 of vendor advances with a **dead** `deduct_down_payments`; 2,486 manual valuation interventions (1,354 posting to the GL); 9 layers linked to cancelled entries; 33.31% of inventory entries not dated on their stock move | Expert 4 |
| **32 PO lines have done receipts with `qty_received = 0`** — a code-level candidate root cause for the price-unit explosion | Expert 4 |

---

## 7. TWO PROCESS FLAGS AGAINST THIS PACKAGE

- **`NEAR-MISS-P01-09`** — the "frozen" brief received **15 new files during the review** (Expert 2). Expert 2's
  own source tables predate the freeze, so its measurements are sound, but **the freeze was declared and not
  enforced.** Content-hash the frozen set next time and hand the digest to the challengers.
- **`GAP-P01-07`** — **41 of 651 tables extracted (6.3%)**, no stated selection rule, no re-extraction check.
  **Every negative in this round is bounded by that 6.3%, and the boundary was never declared.**

---

## 8. THE EXPERTS' OWN DISCIPLINE, RECORDED

Expert 4 logged **five defects it caught in its own work**, including nearly publishing a false correction
after keying `ir_property` on `name` instead of `fields_id`, and reading a background grep at 102 of an
eventual 530 lines. Expert 3 declined to publish *"full-base withholding on partial payments"* as observed
behaviour because the two clean cases show **prorated halves the code cannot produce**, and preserved both
statements unreconciled. Expert 1 ruled out consignment, drop-ship, subcontracting and intercompany **each
with its own control**, and stated that it did **not** sweep `$HOME` or `/Volumes`.

**This is the standard the authoring half of this package did not meet on the GRNI total, the price-difference
conclusion, or the ledger claim.**
