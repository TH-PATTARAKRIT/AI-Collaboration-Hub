# P01 — FUNCTION COVERAGE REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

**This register does not publish a coverage percentage.** Under the project's denominator rule
a percentage requires a verified denominator, and the P01 function universe has not been
proven enumerable. What follows is an explicit statement of what was traced, what was assigned
to an independent expert, and what was not searched at all.

---

## 1. DENOMINATOR STATUS

`UNBOUNDED / NOT YET ENUMERABLE` for the P01 *function* population.

What **is** bounded, with declared pattern, path set and unit, is recorded in the evidence
base §2: the module populations (A and B) and the journal-entry creation-site population (C).
Population C is explicitly a **floor, not a total** — its false-negative modes are declared.

Reason a function denominator was not attempted: the chain crosses at least 211 modules in one
root alone (population B), and no mechanical rule was found that separates "a function that
participates in procure-to-pay" from "a function reachable from one that does". Declaring a
number here would be an author-derived taxonomy presented as a denominator — the exact defect
the project's rules name.

---

## 2. TRACED BY THIS SESSION DIRECTLY

| Capability | Depth | Outcome |
|---|---|---|
| Order confirmation and approval | source read end-to-end | `EV-P01-01`, `EV-P01-03` |
| Order cancellation guard | source read | `EV-P01-02` |
| Order-stage accrual and its reversal | source read end-to-end, both generations | `EV-P01-16`, `EV-P01-17` |
| Receipt valuation entry: guards, accounts, date, failure modes | source read end-to-end | `EV-P01-04`..`EV-P01-08` |
| Bill line account override | source read | `EV-P01-09` |
| Clearing-account reconciliation | source read end-to-end | `EV-P01-10` |
| Price-difference engine incl. history replay | source read end-to-end | `EV-P01-13`, `EV-P01-14`, `EV-P01-15` |
| Reset-to-draft / cancel / duplicate effects on derived journal items | source read | `EV-P01-11`, `EV-P01-12` |
| Asset auto-creation from a bill | source read | `EV-P01-18`, `EV-P01-19` |
| Payment entry generation | source read | `EV-P01-20` |
| FX difference creation point | creation-site enumeration | `EV-P01-21` |
| Inventory revaluation | creation-site enumeration | `EV-P01-22` |
| Cross-company auto-generation, both directions | source read end-to-end | `EV-P01-26`..`EV-P01-31` |
| Vendor down payments in the base capability | source read + caller enumeration across the whole root | see §3 |
| Subcontract receipt valuation | source read | see §3 |
| Company scoping of the P01 object set | mechanical probe, presence-only | `P01_SCOPE_OWNERSHIP_MATRIX.md` |

### Cross-generation coverage

File-level comparison of six core files plus whole-root searches establishing that the
clearing-account model has no runtime presence in the later generation. `EV-P01-24`,
`EV-P01-25`.

---

## 3. TWO FINDINGS RECORDED ONLY HERE

**Vendor down payments are bill-first, and asymmetric with the sales side.**
The down-payment routine has exactly **one caller in the entire root**: a wizard that converts
existing vendor-bill lines into down-payment lines on a purchase order, creating the order if
none exists. There is **no purchase-side wizard that raises an advance from an order**, while
the sales side has a dedicated advance-invoicing wizard.
- POPULATION: callers of the down-payment routine. UNIT: one call site. PATTERN:
  a recursive text search for the routine's own identifier over every source file in the root, excluding test directories → 2 results
  (1 definition, 1 caller). PATH SET: all of `R1`. Cross-checked by enumerating the wizard
  directory of all five `purchase*` modules in `R1`.
- FALSE-NEGATIVE MODES: an indirect call through dynamic attribute access is not matched; a
  caller in a root not searched is not matched (class C).
- Classification: **FACT VERIFIED**, negative claim class **A within `R1`**.
- Significance: the project has added its own advance-payment modules in both custom sets,
  which is evidence the base shape did not fit the business. Their behaviour was assigned to
  the Localization expert.

**Subcontract receipt is a distinct valuation pattern.**
On receipt of a subcontracted item the credit is **split into two** — component cost and
subcontracting service cost — and the valuation price is forced rather than derived. The
source's own comment states that the service cost figure may not represent the real cost of
the service.
- Classification: **FACT VERIFIED** for the split and the forced price, scope `R1`,
  subcontracting-accounting module. **SUPPORTED INTERPRETATION** for its consequences.
- Significance: this is a sixth purchase shape beyond the five in the event-to-GL matrix, and
  it is the only one where the reference source itself documents that a posted amount may not
  be the real cost.

---

## 4. ASSIGNED TO INDEPENDENT EXPERTS

Reported in `P01_AAS03_EXPERT_CHALLENGE.md`. Assigned ≠ covered; where an expert did not reach
an item it stays class C.

| Area | Expert |
|---|---|
| Order/requisition/request lifecycle, bill control policy, three-way matching, partial and over receipt, bill-to-order matching | Functional Design |
| Constraints, indexes, identity, immutability, deletion paths, access rules, company scoping | Database Design |
| Thai withholding tax, Thai purchase VAT, advance payments, backdating and effective dates, payment deductions, multi-currency steps | Integration & Localization |
| Menu/action/view/field enumeration, reversal and correction paths, period-lock enforcement and bypass, landed cost, FX rate selection | Code & UI Architect |

---

## 5. NOT SEARCHED — CLASS C

Recorded so that no reader mistakes silence for absence.

- Vendor portal and any external submission path
- Electronic invoicing and document-exchange paths
- Automated extraction of bills from documents
- Procurement rules, replenishment and automatic order generation
- Budget control on purchases
- Approval-workflow modules
- Reporting and analytic layers
- Scheduled jobs touching purchase, receipt or bill
- Every module in population B not named above (**at least 190 in `R1` alone**)
- Every source root outside the five declared
