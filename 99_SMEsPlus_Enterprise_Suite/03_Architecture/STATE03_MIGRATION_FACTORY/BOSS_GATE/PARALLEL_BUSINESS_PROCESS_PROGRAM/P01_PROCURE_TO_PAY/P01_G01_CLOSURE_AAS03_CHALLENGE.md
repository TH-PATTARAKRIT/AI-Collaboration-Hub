# G01-P01 — TARGETED CLOSURE CHALLENGE (AAS-03 ×4)

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001` · Checkpoint `CP-06`

Four short challenges on the closure package only. **No expert declared a whole-process verdict.**
Every correction below was **re-derived in this package before adoption**.

---

## 1. THE ASSIGNED DISPROOF OF C-1 SUCCEEDED — AND IT CHANGES THE TERMINAL STATE

**C-1 claimed:** broad P01 research can safely stop now.

**Expert 1's finding, verified here to the digit:**

> **Six rounds established what the GRNI account IS. Not one established what is IN it.**

Decomposing the published **13,666 posted items / −฿7,048,692.08** by originating business transaction —
coverage control reproduces both figures exactly, zero residual outside the named classes:

| Origin class | Items | Net THB |
|---|---:|---:|
| `in_invoice` **PO-linked** | 6,297 | 4,071,687,860.09 |
| Stock receipt | 5,306 | −3,395,870,854.60 |
| **UNCLASSIFIED manual `entry`** | **51** | **−1,742,591,244.82** |
| Outgoing `WH/OUT/…` | 665 | 708,164,653.64 |
| `in_invoice` **non-PO** | 298 | 269,689,658.68 |
| Return moves | 112 | 98,319,140.75 |
| **Inventory adjustment** | **716** | **−68,436,934.23** |
| Picking type 3 | 8 | 45,054,545.50 |
| SVL whose stock move is **not `done`** | 182 | 17,891,023.03 |
| `in_refund` | 31 | −10,956,540.12 |
| **TOTAL** | **13,666** | **−7,048,692.08** |

**Only ~45% of gross movement in the account is purchase-order driven.**

### 1.1 ฿1.74 billion of manual reclassification, unmentioned in six rounds

**Verified independently: 51 items across 28 posted manual `entry` moves, net −฿1,742,591,244.82**, none
carrying a bill, a PO or a valuation layer. Their operator-written Thai `ref` text is the evidence:

| Move | Date | Net | `ref` |
|---|---|---:|---|
| `DEPRE2023090003` | 2023-09-30 | −274,297,054.03 | *ปรับปรุงยอดยกมางบการเงิน ปี2566* (restating FY2566 opening balances) |
| `DEPRE2024020038` | 2024-02-29 | −259,411,100.50 | *ปรับปรุงบัญชี 4010008…* |
| `DEPRE2024010057` | 2024-01-31 | −255,957,446.40 | *ปรับปรุงบัญชี 4010008…* |
| `DEPRE2024010058` | 2024-01-31 | −195,708,201.27 | *ปรับปรุงบัญชี 2900000 Goods Receipt Note(GRN)…* |

Expert 1 reports the recurring reason text as *"…**เนื่องจากผูกผังบัญชีผิด**"* — **"because the
chart-of-accounts mapping was wrong."**

> **This is the dated, valued, attested trace of the account-mapping history that `ir_property` cannot
> show — the exact question rounds 5 and 6 left unresolvable. It sat in an already-extracted table for six
> rounds.**

**Adopted. This is the strongest single argument against declaring P01 work exhausted, and it is P01's own
evidence.**

### 1.2 Scrap and inventory adjustment post into the *purchase* clearing account

Mechanism, from source: `stock_account/models/stock_move.py:380-384` falls back to the category's
`stock_input`/`stock_output` when the location carries no valuation account. Locations **14 `Inventory
adjustment`** and **16 `Scrap`** both have NULL `valuation_in/out_account_id` — *positive control: location 15
`Production` carries 1068/1068, so the nulls are configuration, not a parse failure.*

- Inventory adjustments **credit GRNI ฿68,436,934.23** across 716 items.
- **2,257 scrap entries expense to `4010002 Consumption of raw materials`** — **there is no inventory-loss
  account, and scrap is indistinguishable from normal consumption in the P&L.**
- **190 of 477 done return moves produced no valuation layer at all** — cause not established. **RISKY.**

### 1.3 Where Expert 1's own case failed, reported as found

- **Vendor advances are NOT material**: 9 posted unreconciled non-internal supplier payments,
  −฿1,534,955.07, against 14,258 reconciled. **No round warranted** — this narrows `S16-B-02`.
- **Returns do not drive the cost explosion**: 76 PO lines carry a done `to_refund` return, 49 satisfy
  `qty_invoiced > qty_received`, **intersection 0** — latent, not live.
- **But it sharpened the live set**: **18 of the 49** invoiced-not-received lines have
  **`qty_received = 0.000000`** — the exact zero-denominator subset for the missing guard in
  `_get_price_unit`, at unit prices to ฿3,271,028.04. **The firing set is 18, not 49.**

---

## 2. THE C-5 COUNT RESOLUTION WAS ARITHMETICALLY RIGHT AND SEMANTICALLY WRONG

**Expert 2, verified here.** The counts 1,267 / 1,123 / 144 / 74,982 are **SUPPORTED**. The *interpretation*
is **falsified by the engine's own source**:

`stock_account/models/account_move.py:360-362` guards with
`if float_is_zero(unit_valuation_difference * qty_to_correct, …): continue` **before** the row is assigned —
**so no layer can exist with a zero correction.**

Verified: **of all 1,267 price-difference layers, `value == 0.00` on 0.**
*Positive control: 3,865 layers with `value == 0.00` exist elsewhere in the 74,982.*

The two columns measure different deltas: `value` = bill price vs **the receipt layer's own unit cost**;
`price_diff_value` = **PO price vs bill gross price**. So `price_diff_value = 0` means **the bill agreed with
the PO** while the layer was still valued differently. **The 144 carry real money — `value` sums to
−฿5,957,842.04** (abs ฿12,764,989.32).

> **They are the population where billing was correct and valuation was wrong — the diagnostic subset for the
> `_get_price_unit` root cause. P01 filed them as benign residue.**

---

## 3. C-9 BOUNDS ONLY NEGATIVES — TWO UNOPENED TABLES TEST *AFFIRMATIVE* CLAIMS

**Expert 2. Adopted.** *Positive control that these are real: `stock_valuation_adjustment_lines` has a COPY
header and 0 rows (exists, empty); `account_move_line_purchase_line_rel` has no header (does not exist).*

| Unextracted | Rows | Tests which surviving claim |
|---|---|---|
| **`mail_tracking_value`** | **571,522** | *"correction is immutable reversal"*; *"no period lock"*; *"posted after `WHT3%` was zeroed"*. The **only** artefact recording what changed on an already-posted record |
| **`account_fiscal_year`** | **4** | *"no period lock of any kind"* — a **second locking surface never enumerated** |
| `ir_model_data` | 107,873 | module ownership of the account-1173 configuration |

### 3.1 The period-lock claim: enumerated after challenge, and it survives

Every locking surface in the archive was then enumerated — there are exactly **two tables**:

| Surface | Content |
|---|---|
| `res_company.period_lock_date` / `fiscalyear_lock_date` / `tax_lock_date` | **all NULL** |
| `account_change_lock_date` (the lock-date wizard) | **0 rows** |
| `account_fiscal_year` | **4 rows** — Y2023-2024, Y2024-2025, งบเพิ่มเติม 25, Y2026 |

**A fiscal year defines period boundaries; it is not a lock.** The corrected claim — **no lock date is set
anywhere** — **survives, and is now proven by enumeration rather than asserted from one table.**
The earlier phrasing *"no period lock of any kind"* was a universal tested against **one** surface.

---

## 4. EXPERT 4 — THE P03 HANDOFF'S CENTRAL SENTENCE WAS A DOCSTRING

**Adopted in full; re-derived from source.** `purchase_mrp/models/account_move.py:10-14` contains **no kit
predicate** — no `bom_type`, no `_bom_find`, no `bom_line_id`, no `phantom`. The filter
(`layers.filtered(lambda svl: svl.product_id == self.product_id)`) is **unconditional**. **"Kit" appears only
in the docstring**, and the module's other three overrides **all** gate on `bom_type='phantom'`.
`'auto_install': True`, so it is not opt-in.

**"LATENT here" was live**: 23 bill lines name a different product than their PO line, 18 valid, and **13 have
layers actively dropped by the filter — no kit involved**. Positive control 14,335; synthetic injection flips
0→1.

**The kit census repeated a withdrawn defect**: BoM `type` is mutable, so a current-state census **cannot see
a reverted row** — the same flaw withdrawn for `ir_property` one round earlier. The conclusion survives only
on a control P01 never ran: moves with `bom_line_id` **and** `purchase_line_id` = **0 of 34,492**.

**P01 named 1 of 4 overrides.** One undisclosed override **wraps `_get_price_unit`** (the cost-explosion root
cause); another **rewrites `qty_received`** (its entry condition).

**Boundary corrected — P01 was under-stepping**: no predicate separates the kit case from the non-kit case, so
P01 **retains** the unconditional filter and its 13 live rows; P03 receives only the kit question. **"LATENT"
is removed** — a severity word pre-ranks another process's item before that process has measured anything.
*Recorded as `ERR-P01-48`.*

---

## 4A. EXPERT 3 — THE P08/P11 SENTENCE WAS FALSE IN BOTH HALVES

**Adopted; re-derived here.** Of 1,267 price-difference layers, **1,175 (92.7%) still point at the vendor
bill — no GL entry was ever made**; only **92** point at an `STJ` valuation entry.

The 92 that posted move inventory **down**: `1141001 Raw material` **net −฿7,267,712.95**,
`2900000 GRN` +฿7,270,276.79, and **`4010002` (expense_direct_cost) −฿2,563.84**.

- **"Capitalised into inventory"** — false for 92.7%, and **directionally wrong** for the 92.
- **"No P&L variance line"** — **falsified**: 4 of 22 categories point `stock_input` at a P&L account and it
  fired twice in-path; and **1,082 of the 1,175 bill-only layers sit on a bill line posted to P&L**.
- **"In the observed path"** — a description, not a declared set: 4 categories inherit `cost_method='standard'`
  and are structurally invisible; **anglo-saxon being FALSE is the actual reason no named variance line
  exists**.

Expert 3 also confirms the **WHT boundary is correctly held** — a statutory-wording sweep of the closure brief
returns only two procedural hits — but flags that **the six P07 items were counted and never enumerated** in a
closure-only document. **They are now enumerated in the P11 handoff.**
*Recorded as `ERR-P01-49`.*

---

## 5. WHAT NO EXPERT OVERTURNED

Expert 1, explicitly: *"Nothing above overturns a published C-2..C-8 finding. Every item is additive."*
The receipt→valuation→GL execution, the mixed policy population, immutable reversal, the AP profile, the
`_get_price_unit` root cause, the WHT rate-record finding and the `S16-B-05` deletion hypothesis all stand.

**The freeze is challenged on completeness, not on correctness.**
