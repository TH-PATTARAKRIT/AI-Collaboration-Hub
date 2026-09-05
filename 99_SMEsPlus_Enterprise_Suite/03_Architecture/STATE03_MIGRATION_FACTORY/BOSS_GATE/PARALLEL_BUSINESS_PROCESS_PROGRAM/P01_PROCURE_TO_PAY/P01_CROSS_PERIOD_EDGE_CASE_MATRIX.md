# P01 — CROSS-PERIOD EDGE CASE MATRIX

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Directive §25: the high-risk **combinations**, each captured across seven truths.
**None of these was executed.** Every row is a reading of source and deployed configuration, and
is therefore a **test to run**, not a test that passed.

Legend — `SRC` source-derived · `DB` deployed-configuration-derived · `EXP` independent expert ·
`RUN` requires runtime.

---

## 1. THE COMBINATIONS

### C-01 — Receipt in a locked period, bill in an open period

| Truth | v16 deployment | v19 deployments |
|---|---|---|
| Business | goods arrived in the closed period | same |
| Inventory | quantity in the closed period | quantity in the closed period |
| Liability | clearing raised — but the entry is **re-dated** into an open period, not refused | **no entry exists at all** |
| Tax | n/a at receipt | n/a |
| Journal | exists, carrying a **date the system chose** | none |
| Period | the goods' economic period and their accounting period **differ by construction** | the receipt has no accounting period |
| Reversal | reversible | nothing to reverse |

Basis: `SRC` + `DB`. The re-dating behaviour is being independently re-derived by an expert.

### C-02 — Receipt returned after the bill is posted

Goods leg and money leg are separate events: the return is valued as an outgoing movement
against the clearing account in v18, and **produces no accounting effect at all** in the v19
deployments. The payable is cleared only by a credit note. `SRC`.
**Risk:** in the v19 deployments the inventory reduction and the payable reduction have no
common accounting artefact linking them.

### C-03 — Bill reset to draft after it has been reconciled

The derived interim and price-difference journal items are **deleted**, not reversed. Whether
the reconciliation is broken, refused or silently severed is under independent challenge —
one expert is specifically tasked with attempting to **disprove** that lineage is destroyed.
`SRC` + `EXP`.

### C-04 — Partial bill + partial payment + withholding

The compounding defect in the installed withholding path fires **per partial payment**, so this
combination is where it does the most damage. Under independent disproof challenge. `SRC` + `EXP`.

### C-05 — Landed cost after period close

Assigned to an independent expert. Landed cost is **installed in all three deployments**, so
this is live, not latent. `EXP`.

### C-06 — Subcontract receipt before the vendor bill

**Latent in every readable deployment** — no subcontracting module is installed anywhere. The
source behaviour splits the receipt credit into component cost and service cost, with the
source's own comment warning the service figure may not be the real cost. `SRC` + `EXP`.

### C-07 — Vendor refund after the goods have been consumed

In v18 the price-difference engine has an explicit refund branch keyed to the reversed entry,
and a hand-written exception exists for re-receipt of returned goods — evidence the general
model is under-specified. In the v19 deployments there is no valuation entry to correct. `SRC`.

### C-08 — Backdated vendor bill

The lock does not refuse; it re-dates. The custom effective-date tool that would force a date
**CORRECTED (`ERR-P01-15`): the subcontracting family IS installed** — in the fourth database, which this package wrongly recorded as unreadable. An expert reports **zero subcontract transactions** there, so the status is **INSTALLED BUT NOT EXERCISED**, not latent. `SRC` + `DB`.

### C-09 — Cancel after the tax report has been filed

Derived journal items are deleted. What survives, and whether the tax report can still be
reproduced, is the substance of the lineage disproof task. Statutory consequence is **P07's**.
`SRC` + `EXP`.

### C-10 — Receipt and consumption both inside a period that then closes, bill in the next

**The defining v19 case.** Neither the asset nor the obligation ever entered the closed period.
The period closes clean and complete, and is wrong by the full value of everything received and
consumed but not yet billed. `SRC` + `DB`.

### C-11 — Cross-company auto-generation across a period boundary

Approving an order, or posting a bill, whose vendor resolves to another company creates a
document **in that other company**, as superuser by default, optionally auto-posted — into
whatever period that company is in. **Now known to be installed and live in both v19
deployments.** `SRC` + `DB`.

### C-12 — Advance paid in one period, goods billed in the next

The advance is booked to an **expense** account by default. If the advance is expensed in
period 1 and the goods expensed again in period 2, both periods are overstated unless the
netting works. `SRC`, netting is `RUN`.

---

## 2. THE SEVEN TRUTHS, SUMMARISED ACROSS ALL COMBINATIONS

| Truth | Weakest point found |
|---|---|
| **Business truth** | Survives everywhere — the documents persist |
| **Inventory truth** | Sound operationally; **has no ledger representation at all in the v19 deployments** |
| **Liability truth** | Exists only from the vendor bill onward; the received-not-billed obligation has two candidate representations in v18 and **none** in the v19 deployments |
| **Tax truth** | Withholding compounds across partial payments in the installed path; form mapping is inverted between shipped copies |
| **Journal truth** | Derived items are **deleted** on correction rather than reversed |
| **Period truth** | The lock **re-dates instead of refusing**, so cut-off tests on entry dates are self-confirming |
| **Reversal truth** | Return and credit note preserve history; reset-to-draft and cancel do not |

---

## 3. EXECUTION PRIORITY

Ranked by irreversibility and silence, not by likelihood. **None has been run.**

| Rank | Case | Why first |
|---|---|---|
| 1 | **C-10** | Silently omits an entire period's purchases; needs only a receipt, a consumption and a period close |
| 2 | **C-11** | Crosses a company boundary with unproven ownership; **live in both v19 deployments** |
| 3 | **C-03** | Destroys accounting lineage if the disproof fails |
| 4 | **C-04** | Over-withholds real money from real vendors, per partial payment |
| 5 | **C-01** | Establishes whether re-dating is universal or path-dependent |
| 6 | **C-12** | Double-expense across periods; the module is installed everywhere |
| 7 | **C-05** | Landed cost is installed everywhere and its period behaviour is unknown |
