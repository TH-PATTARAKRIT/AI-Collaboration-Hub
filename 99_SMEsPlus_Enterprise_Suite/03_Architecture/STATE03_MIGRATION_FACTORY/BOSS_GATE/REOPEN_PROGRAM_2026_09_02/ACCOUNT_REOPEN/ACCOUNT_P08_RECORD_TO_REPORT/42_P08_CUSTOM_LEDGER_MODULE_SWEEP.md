# P08_CUSTOM_LEDGER_MODULE_SWEEP

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · Phase B · `CP-T03`

## 1. Denominator — re-derived, and the earlier figure corrected

| | Count | Basis |
|---|---|---|
| Custom modules with a manifest | **65** | verified two ways: a manifest search and a directory listing return the same number, so no module lacks a manifest and none is nested deeper |
| Non-module archives, not opened | 3 | `C NOT YET SEARCHED` — the 65 is therefore a **floor** |
| **Ledger-touching modules** | **30** | union of two declared criteria: own source references a ledger model or table; **or** the manifest declares a direct dependency on an accounting-family module |
| Already examined in prior P08 work | 9 | |
| **Swept in this phase** | **21** | |

**Correction to the package's earlier figure.** The prior session reported **21** ledger-touching custom modules. That number is the **work-queue length**, not the population: the ledger-touching population is **30**, of which 9 were already examined. `P08-CONTRA-20` — the earlier figure understated the population by 9.

The dependency criterion caught **6 modules the source-reference criterion missed**, which is the reason for the delta. A module that touches the ledger only through an inherited accounting model can carry no ledger token in its own source.

## 2. Deployment gating — the finding that governs every severity below

The sweep's own top unknown was *which of these are actually installed*. **Settled from the deployed module registries.**

| | Count |
|---|---|
| Swept modules | 21 |
| **Installed in at least one deployed database** | **9** |
| Uninstalled or absent in all three | 12 |

| Installed | `DB-SM` (16.0) | `DB-BK` (19.0) | `DB-EV` (19.0) |
|---|---|---|---|
| `scgl_purchase_advance_payment` | **yes** | **yes** | **yes** |
| `dev_print_cheque` | **yes** | **yes** | **yes** |
| `account_discount_catalog` | — | **yes** | **yes** |
| `invoice_promptpay` | — | **yes** | **yes** |
| `scgl_account_reports` | **yes** | — | — |
| `print_voucher_request` | **yes** | — | — |
| `equipment_sequence` | **yes** | — | — |
| `bi_print_journal_entries` | **yes** | — | — |
| `full_summarize_bills` | **yes** | — | — |

**The most severe code findings are largely not deployed.** The advance-expense module — which cancels posted entries by raw state write, and exposes an unvalidated posting wizard to every user — is **absent or uninstalled in all three**. So are the commission module, the brand module, the petty-cash module and the two auto-posting modules.

## 3. Live findings — installed modules only

| ID | Module | Finding | Deployment |
|---|---|---|---|
| `B-13` | `scgl_purchase_advance_payment` | **Vendor bills created under elevated privilege**, from a wizard whose access row grants every internal user full rights. The elevation is real; it is bounded by needing write access to a purchase order, which is stated rather than overclaimed | **live in 3 of 3** |
| `B-26` | `dev_print_cheque` | **Cheque number is unvalidated free text** — no sequence, no uniqueness, no state gate. Cheque print-format records are **deletable by the lowest accounting group** | **live in 3 of 3** |
| `B-12` | `account_discount_catalog` | **A posted invoice can be re-discounted from an always-visible button.** Verified against source that the core does not stop it: adding a line to a posted entry is not refused, and the discount attribute is in none of the protected sets, so the write passes the period, tax and settlement checks | **live in 2 of 3** |
| `B-05`/`B-06` | `scgl_account_reports` | **The statutory value-added-tax register admits a row only when the tax group's translated name equals a single-key English literal**, and the zero/exempt register filters at entry level on a line-level query while an inner join silently drops unpartnered tax lines | **live in the production-scale database** — see §4 |
| `B-24` | `print_voucher_request` | **The withholding figure on the vendor-facing document is recomputed from current master data, not read from the ledger.** Reprinting a historical certificate yields today's rate | **live in 1 of 3** |
| `B-20` | `equipment_sequence` | **Every internal user reaches numbering-object deletion under elevated privilege**, and the module feeds asset references | **live in 1 of 3** |
| `B-28` | `bi_print_journal_entries` | A journal-entry report with **no posting-state gate** — a draft entry prints as a totalled journal document | **live in 1 of 3** |

## 4. The statutory register defect, tested against the deployed data

The custom register admits a row only when the tax group's name equals exactly a single-key English literal. Tested against the tax groups of the database where the module is installed:

| Tax group | Stored name |
|---|---|
| VAT 7% | `{"en_US": "VAT 7%"}` — **single key** |
| TAX 1%, 2%, 3%, 5% | single English key each |
| Taxes | `{"en_US": "Taxes", "th_TH": "ภาษี"}` — **two keys** |

**Two precise conclusions, and neither is the one the mechanism alone would suggest:**

1. **The register currently renders.** The value-added-tax group has a single key, so the equality holds. The failure mode of an empty register is **not realised in this database today**. `CONTRADICTED` as a present-tense claim about this install.
2. **The mechanism is nonetheless live, and demonstrably so.** An adjacent tax group in the same database **is** translated and carries two keys. One translation of the VAT group's name — an ordinary localisation act — makes the register render **empty, with no error**.
3. **Five of the six tax groups are excluded from the register unconditionally** by the hard-coded rate literal. Any rate that is not 7% is silently outside the statutory register and its totals.

This refines, rather than confirms, a finding recorded by the tax process: the empty-register mechanism is real and one edit away, and the rate-exclusion defect is **already in effect**.

**No statement is made about what Thai law requires.** `HOLD — STATUTORY EVIDENCE REQUIRED`, routed to the Accounting-Tax track and to P07.

## 5. Findings on code that is present but not deployed

Recorded in full, at reduced severity, because the code exists and may be installed later. The most consequential: posted entries cancelled by a raw state write that skips settlement removal, analytic-line removal and payment cancellation while the period lock still applies; an unvalidated clearing wizard exposed to every user; a payment-integrity guard that targets a hook the current accounting kernel does not call; a petty-cash account mechanism whose override hooks a method that no longer exists.

## 6. The structural finding of this phase

**Five of the twenty-one modules carry a mechanism that is declared, visible in the interface, and does not execute** — a dead override, a sequence whose data file is commented out of the manifest, a report model with no backing relation, a report handler registered under a colliding name, and a settings class declared on the wrong model.

In each case **the control appears present to anyone reading the module and is absent in the running system.** That pattern threatens a reliance conclusion more than any individual bypass, because it is invisible to exactly the review method most likely to be applied — reading the code.

## 7. Enumeration discipline

Every pattern in the sweep carries a positive control. One control **failed and was replaced rather than accepted**: the first choice for the control-bypass pattern did not fire, so the pattern was re-validated against the reference accounting kernel, where it returns 22 and 63 matches in the two core files. The 4-hit result across the 21 custom modules is therefore **a real scarcity, not a dead pattern**.

Two zero results were re-run in a second form, per the standing rule, and both proved positional rather than pattern failures.
