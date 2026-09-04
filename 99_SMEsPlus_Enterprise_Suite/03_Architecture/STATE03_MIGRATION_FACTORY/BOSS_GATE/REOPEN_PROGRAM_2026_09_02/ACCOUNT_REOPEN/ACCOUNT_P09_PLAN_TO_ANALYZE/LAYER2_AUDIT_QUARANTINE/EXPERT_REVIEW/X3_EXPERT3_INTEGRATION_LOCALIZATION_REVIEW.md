# X3 — AAS-03 EXPERT 3 · INTEGRATION & LOCALIZATION · ADVERSARIAL REVIEW
**LAYER 2 — AUDIT QUARANTINE.** Session SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001.
Independent reviewer, disjoint assignment. All four roots in its brief resolved correctly; no path correction required.

## A. CORRECTIONS RETURNED AGAINST THE RESEARCH TEAM

**X3-COR-01 — E00's custom-root counts do not match a module enumeration.** Directory-entry counts of 68 / 57 / 50 against loadable-module counts of 65 / 57 / 47. **The research team confirmed the reviewer is right on the unit**: the entry counts include archive files that are not modules. E00 was corrected in place. This is a textbook instance of the project's own UNIT clause — a count was stated in the wrong unit for the claim it bounded.

**X3-COR-02 — a *statutory* Thai module varies by deployment copy.** The multi-line withholding-tax module is present in two custom roots and **absent from the third**. This is the same class of fact as COR-P09-06 but for a statutory capability rather than a management dimension, so the severity is higher: whether a required Thai capability exists at all is a property of which copy is deployed, and which copy is deployed is class **D**. Routed to the Accounting-Tax track as a hold item; not decided here.

**X3-COR-03** — cross-process ownership and inter-company handling were open scope, not correction targets. No prior claim is contradicted by sections B/C.

## B. NEW FINDINGS

**X3-01 — a bill line's allocation can be silently overwritten by a rule match when the account is reclassified, discarding the value inherited from the order.** Traced end to end:
- the order-to-bill value builder (`purchase/models/purchase_order_line.py:551-568`) does **not** carry the allocation at all;
- the real propagation is a compute (`account/models/account_move_line.py:1070-1091`) declared to depend on the account, the partner and the product — **not** on the order line;
- the order-to-bill copy is guarded by "only if the bill line has none" (`purchase/models/account_invoice.py:537-542`), so first creation copies correctly;
- the compute's assignment (`account_move_line.py:1091`) is `related | rule_result or existing`. On a later **account reclassification** — a routine accountant action — the compute re-runs, the order guard now blocks the re-copy, and **if a rule matches the new account its result overwrites the inherited value outright**;
- no conditional-recompute guard exists for the allocation field, in contrast to the account and tax fields which do have one (`:1147`, `:1154`, `:1195`);
- per EV-P09-102, independently re-confirmed at `account_move_line.py:393-395`, the overwrite produces **no chatter entry**.
The identical shape was independently confirmed for expenses at `hr_expense/models/hr_expense.py:516-527`.
**This answers the brief's question directly: the order's allocation survives to the bill, and it can be silently superseded later without any warning that it now differs from the order.** Mechanism CONFIRMED from source; the live trigger was not executed.

**X3-02 — asset accounting is the one process with an explicit, coded ownership boundary.** `account_asset/models/account_asset.py:528-534` re-propagates an updated allocation only to **draft** depreciation entries, with a source comment naming the reason. It is the only place among the eight processes examined where "does a downstream override survive to posted documents" is answered **no** by an explicit state guard rather than emerging as a side effect of a dependency list.

**X3-03 — inter-company mirroring silently drops the entire allocation at the company boundary.** `account_inter_company_rules/models/account_move.py:108-160`:
1. `:146` — every allocation key whose axis value carries a company is identified;
2. `:148-155` — those keys are **dropped**; only keys referencing company-less axis values survive;
3. `:157` — the mirrored line's allocation is set **only if** the receiving company has its own rule match or some company-less key survived. If neither holds, **the mirrored line carries no allocation whatsoever**;
4. the module's own test asserts exactly this (`tests/test_inter_company_invoice.py:147-159`, asserting the mirrored line's allocation is empty);
5. where the receiving company does have a rule match, that result is the **base** and surviving keys are merged on top — so the receiving company's own default silently outranks the sending document.
No warning, no message, no exception on either path. Class A, corroborated by the module's own test suite. **This is the same silence pattern found inside a single company at EV-P09-029, now confirmed across the company boundary.**

**X3-04 — no export or e-invoicing path carries management data outside the system, within the searched pattern.** All modules matching the three export-family name patterns at root depth were swept for the analytic pattern across code and view files: **zero hits**. Class **A** for that pattern and path set. Statutory exports under other naming, and any Thai-specific export, are class **C** — though moot for Thai specifically, given section C.

**X3-05 — the Thai withholding-tax custom modules have zero management-accounting references, in every copy.** Five module names across three roots (14 existing copies), pattern covering analytic, budget, cost centre and department, code and view files: zero hits everywhere. Class **A** within that pattern and path set. **Thai withholding tax is structurally independent of the management-accounting layer in this codebase.**

## C. THAI LOCALIZATION ENUMERATION

Pattern declared: module name containing the Thai locale prefix at root depth in the reference root, and the case-insensitive Thai substring in the three custom roots (one unrelated match excluded as a false positive). Content pattern: analytic, budget, cost centre, cost center, department — across code and view files.

**10 of 10 Thai-named modules — 2 in the reference root, 8 in the custom roots — return zero hits, in every copy where each exists.** Class **A** within that stated pattern and path set.

### HOLD / EVIDENCE REQUIRED — routed to the Accounting-Tax track
- **HOLD-TH-01** — whether Thai statutory practice requires cost-centre or department segregation in management accounts, VAT reporting or withholding-tax certificates is **not evidenced anywhere in the searched code**. This session makes no claim about whether that silence is a gap against a real requirement or a correct reflection of no requirement. A named statutory citation is required; a code search cannot settle it.
- **HOLD-TH-02** — the department-dimension custom module is not Thai-named but tracks the same deployment-copy uncertainty. Whether Thai cost-centre practice is meant to be satisfied through it is a design question for the Accounting-Tax track.
- Any Thai person, company or vendor name appearing in demo data, fixtures or sample views is **candidate / UNVALIDATED**; none was transcribed.

## D. CROSS-PROCESS OWNERSHIP (summary; full table in `P09_CROSS_PROCESS_OWNERSHIP`)
Purchase→bill and sales→invoice share one host compute with a copy-on-empty guard and **no protection against a later rule-driven overwrite**. Expense shares the same shape. Asset is bounded by an explicit draft-only state guard. Inventory copies the value faithfully but discards the ledger link. Manufacturing originates its own assignment from work-centre master data and inherits from no document. Bank reconciliation copies from the matched ledger row, else falls to rules — same overwrite shape, not independently traced for a state guard (class B). Tax inheritance is conditional (reproduced from prior evidence, not re-verified).

## E. ADVERSARIAL VERDICT — CH-CAND-05: **DISPROVED** as an exposure claim

**The mechanism is confirmed and is stronger than the research team stated.** The view's allocation column is built by wrapping an array of **all** axis columns in a set-returning expansion (`account_reports/models/account_analytic_report.py:118-120`), and the axis list comes from an unfiltered, elevated, system-wide search of every root axis in the database (`analytic/models/analytic_plan.py:100-105`). The multiplication factor is therefore **the total count of root axes defined anywhere**, not the number the record actually populates: every management record becomes exactly that many rows, each repeating the same balance, debit and credit.

**But the exposure does not follow.** The reviewer enumerated callers rather than reasoning abstractly:
- a whole-root sweep for the five relevant option keys and method names found **exactly one** call site that ever sets the grouping option (`account_analytic_report.py:71` and `:82`);
- in **both** branches the option is set in the same forced-options dictionary as the restricting axis-value list — there is no path that sets one without the other;
- the domain builder (`:231-242`) unconditionally adds the restricting filter whenever that list is present, and the base query builder always consults it;
- the allocation mixin special-cases the reporting context to fall back to a scalar comparison, consistent with the view's single-value column;
- the cash-basis variant builds a separate view but is reached only through the same chain.

**Verdict: for the enumerated caller set — exhaustive within the reference root — no caller reaches the view without the restricting filter. The candidate's exposure claim does not hold in the scope searched.**

**Caveats attached, so this is not read as full closure:**
1. not executed against a running database;
2. **a new residual surfaced while disproving it**: the restricting list carries integer axis-value ids compared against a column wrapped as a JSON scalar. Whether that comparison matches correctly or silently returns nothing — a *correctness* failure rather than an exposure — was **not decided from source**, class **C**;
3. custom modules in the three tenant roots that might extend the report layer were not exhaustively cross-checked — a confirming sweep returned no hits, class **C** for the residual.

## F. SEARCH BOUNDARY
22 enumerated command groups across four roots, including full reads of the analytic report layer, the inter-company mirroring method and its test file, the purchase and sales propagation overrides, the host compute and inverse, and a 3×8 module-by-root matrix for the Thai enumeration; plus explicit declaration of what was **not** searched, each with a class. **No prohibited verdict vocabulary used.**
