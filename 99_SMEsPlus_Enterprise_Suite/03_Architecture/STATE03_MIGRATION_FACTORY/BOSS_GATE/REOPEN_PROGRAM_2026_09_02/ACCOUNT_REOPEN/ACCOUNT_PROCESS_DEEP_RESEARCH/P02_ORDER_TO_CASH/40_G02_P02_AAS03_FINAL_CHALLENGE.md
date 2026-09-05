# 40 — G02-P02 FOUR AAS-03 INDEPENDENT CHALLENGES

`LAYER 2 — AUDIT QUARANTINE.` Prompt §9. Baseline `ff8be51`.

Four disjoint experts, run **after** primary closure work, each given a distinct scope and a mandatory
falsification assignment. **None issues PASS/FAIL.** Each was told that finding nothing is a failure of
the review.

**Every finding below was re-derived by P02 against primary source or live read-only measurement before
adoption.** Nothing is adopted on an expert's assertion. Where an expert's claim did not survive
re-derivation it is marked as such.

---

## 1. Outcome

| Expert | Scope | Confirmed contradictions raised | Against work published |
|---|---|---|---|
| **1 — Leader Functional Design** | lifecycle completeness, 8 scenarios, delivered-not-invoiced, returns/credits, revenue-vs-billing | **`C-34`** | **this round** |
| **2 — Leadership Database Design** | the denominator, identity key, controls, every zero | **`C-43` … `C-47`** | **the package headline** |
| **3 — Lead Integration & Localization** | Thai tax, scope ownership, intercompany, peer handoffs | **`C-35`, `C-36`** | earlier rounds |
| **4 — Lead Code & UI Architect** | custom overrides, UI-vs-data, runtime reachability, `C-04`, idempotency, period lock | **`C-37` … `C-42`** | **four of six this round** |

**12 confirmed contradictions. Ten of the twelve are against work published in this round or in the
package headline.** By contrast this round self-caught four instrument defects (`RE-25` … `RE-28`).
**The ratio is 12 : 4 in favour of independent challenge**, consistent with every prior measurement in
this programme.

---

## 2. Expert 1 — Leader Functional Design

**Supported.** Independently re-derived and reproduced: the credit-control advisory finding including
the discarded `with_company` expression; `P02-F-34d`'s citation; **`34` §2's arithmetic to the digit**
(every row's four buckets sum to its line count, and 3,593 reproduces); the completed-delivery
immutability finding in both generations; and `P02-F-38a`'s v19 relabel.

**Missing.** Early-payment / cash discount is **absent from the entire package** (zero hits across all
files) though it exists in both roots as a settlement-triggered event that debits a discount account and,
in `included` mode, **creates tax lines** — retroactively reducing output VAT after the tax invoice was
issued. Customer advance/deposit has **no spine stage** although the registers carry it four times. The
payment-triggered order path is unanalysed. No service / performance-obligation scenario exists among
the eight.

**Risky.** Six of eight scenario negatives still rest on one instrument and two generations;
`P02-F-34c` is a business conclusion drawn from one column.

**Challenged — `C-34` CONFIRMED.** `qty_invoiced` counts **drafts**
(`sale/models/sale_order_line.py:916-924`); the accounting counter `qty_invoiced_posted` exists and is
**not stored**. Re-measured on `iSMEs` with a posted-only join: **delivered-not-invoiced 1,145, not 47**
— a **24× understatement** — and **`P02-F-34b`'s direction reverses**. Adopted and corrected in `34`.

**Not adopted:** `CH-5` (segment by invoice policy) is **accepted as correct but not executed** —
`invoice_policy` is not on `sale_order_line` (verified: column absent), so it needs a product join.
Recorded as `P02-F-34e`, an open action, not a finding.

## 3. Expert 2 — Leadership Database Design

**Supported, and this is the strongest corroboration the package has received.** The **39-artefact file
population reproduced exactly under a third, independently written instrument** — extension-scoped
`find` plus magic-byte/zip-member test, rather than signature-over-all-files — with **zero difference in
both directions**. The arithmetic reproduces to the digit. `RE-25` was independently confirmed as
correctly diagnosed. Cloud-placeholder and unmounted-volume false-negative channels were tested and are
**empty**. `P02-F-28d`'s zero was tested against its most obvious confound (module absence) and survives.

**Challenged — `C-43` … `C-47`, all CONFIRMED. Two of them change the headline.**

- **`C-43`** — in 14.0 the `display_type` selection admits only `line_section` and `line_note`;
  **`cogs` is not a member**. **80.69% of the published denominator is a generation where the zero is a
  schema fact.** Re-scoped to **493,277 marker-capable lines, 15 databases, generations 16/18/19**.
- **`C-44`** — **seven differently-configured live databases share one `database.uuid`**, and two live
  19.0 uuids sit outside the population. uuid is a **restore-lineage key**. **≥19 uuids, ≥26 instances.**
- **`C-45`** / **`C-46`** / **`C-47`** — artefact column missing; "measured, not inferred" withdrawn;
  file path set closed but **population not closed**.

**Expert 2's final report added two more, both confirmed, and they are the most serious in the package:**

- **`C-48`** — the closure sweep is **blind to plain-SQL dumps**, and the one it missed had **already
  been added to the population by `22` as an explicit correction**. A later round silently reversed an
  earlier round's correction. **Count ≥ 40.** And *"two instruments, same 39"* was not corroboration:
  **all three instruments shared the blind spot.**
- **`C-49`** — **`P02-F-28a` is refuted on its own example.** All three `iEVING` artefacts share one
  `ir_config_parameter` row with `create_date` identical to the microsecond; the uuid was rotated five
  minutes after a backup. **One lineage, not two databases — the name key would have been right.**
  `P02-F-28a` **WITHDRAWN**.

**Expert 2 is the reason this package can be relied on at all.** It attacked the population from four
angles, **corroborated what held under an independent instrument**, reported its own unfinished sweep as
unfinished rather than as a zero — and then, when that sweep completed, **returned to correct its own
earlier report**. That is the behaviour the round asked for and did not itself always achieve.

**Method note P02 adopts.** Expert 2 reported its format-width sweep as **unfinished rather than as a
zero**, and published the predicate's positive control. That is the standard this package asks for and
had not always met.

## 4. Expert 3 — Lead Integration & Localization

**Supported.** Every v18-root Thai fact re-derived exactly: the 27-account chart, the group-less
zero/exempt VAT taxes, the sign defect, the withholding tag asymmetry, and the statutory export printing
the accounting date under "Invoice Date" — the last confirmed **generation-stable**. It also ran a
control that **refuted its own hypothesis** about the WHT wizard gate and dropped it.

**Challenged — `C-35`, `C-36` CONFIRMED.** The **v19 Thai chart is 144 accounts, not 27**, and supplies
the down-payment account, undue output VAT, doubtful-debt allowance, the stock valuation account, and
`tax_exigibility` — four published negatives re-qualified. **The refutations sit inside P02's own
declared PATH SET**, so they bite without any unreadable module. And `06` line 70 still carried a
`VERIFIED ABSENCE` that `27` §4 had withdrawn — *a revision log is not a correction*, recurring.

**Strengthened rather than refuted:** `P02-F-50` (sale-side withholding reaches no report) now holds
against the **readable custom estate** as well, which CA-05 had left as routing rather than evidence.

**Risk P02 adopts as a routing constraint, not a finding:** `DC-09-04` (no write-off to an arbitrary
account) would, in this estate, remove the only sale-side WHT posting path.

## 5. Expert 4 — Lead Code & UI Architect

**Supported.** Verbatim re-derivation of the v18 guard, the v19 fallback, the onchange census, the
lock-date cap, the absent idempotency guard and its correct `NOT FOUND IN SEARCHED SCOPE` label, and both
`32` controls. It also reproduced `33` §2's lab table exactly.

**Challenged — `C-37` … `C-42`, all CONFIRMED; four against this round's own work.**

- **`C-37`** — a **second raise sits outside the `real_time` branch** and can fire on the exact state
  cited. "One-directional" is true of one branch, not of the method. **The aggregation failure `SC-19`
  names, inside the section that names it.**
- **`C-38`** — `SC-18`'s table was described as **whole-tree** and reproduces only under an
  **undeclared `*.py` filter** (44→2, not 1→0). Verdict survives; the description was not the execution.
- **`C-39`** — v19 removed **the fields the guard protected**, not merely the guard.
- **`C-40`** — the combo-tax refutation holds on the sale-order route only; the **direct-invoice route
  applies product taxes with no combo test**, so the P04 defect class survives there.
- **`C-41`** — the runtime population was chosen **by container name**; a third container holds **two
  more 19.0 databases**, one with the split flag **on**. Verdict survives across 9; denominator did not.
- **`C-42`** — `33` §5.9 as scoped tests a **determined** outcome; `03` §6 already named the real
  mechanism. The authorisation request was rewritten.

**Also raised, accepted, not yet executed:** the POS invoice channel is absent from the package;
`product_brand_sale` **fully replaces** `_create_invoices` and was not dispositioned in `32`; `01` carries
no source-scope declaration though `31` §4 establishes the bound; and `P02-F-08b` describes **2 of 5**
sequence-reset cases.

---

## 6. What The Challenges Did Not Break

Stated because a challenge round that only reports damage is not calibrated:

- The **39-artefact file population** — attacked directly by Expert 2 with an independent instrument and
  **survived exactly, in both directions**.
- **All published arithmetic** — recomputed by two experts, reproduced to the digit.
- The **zero-COGS direction** — every expert accepted it; the correction is to its **denominator and
  scope**, not its sign.
- `P02-F-28d`'s zero as **not** a module-absence artefact.
- `P02-F-50`, `P02-F-51`, `P02-F-52`'s first clause, and the absent Outbound Stock role — **hold in both
  generations**.
- `RE-25` — independently confirmed as correctly diagnosed.
