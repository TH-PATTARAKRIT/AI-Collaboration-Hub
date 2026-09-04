# E01 — EVIDENCE CORRECTIONS AND EXTENSIONS (LAYER 2 — AUDIT QUARANTINE)

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001
**Companion to:** `E00_PRIMARY_EVIDENCE_BASE.md`
**Classification:** LAYER 2 — AUDIT QUARANTINE.

This file carries (a) corrections that overturn or narrow a claim in E00 or in a research brief, and (b) extensions that add evidence E00 did not reach. Corrections are listed first because the project standard weights a reviewer-originated correction above an author-originated claim.

Four evidence strands ran in parallel against the primary source with disjoint assignments. Each was instructed that a wrong path in its own brief must be reported as a finding. **Three of the four returned a correction to the brief that tasked them.** That is recorded here as a control result, not as an incident.

---

## PART A — CORRECTIONS

### COR-P09-01 — The brief's producer list under-counted the true producer set by 5 modules. (Corrects the session's own scoping.)
The cost-object brief named 13 candidate producer modules. The tasked researcher refused the list, ran the three declared patterns over both reference roots, and returned a **57-module** union in the primary root, then narrowed it by a *direct-instantiation* pattern to the true producer denominator.

**True producer denominator: 9 modules that literally create an analytic line outside tests.** Five of them were absent from the brief: a timesheet-from-leave generator, a timesheet grid tooling module, a helpdesk timesheet wizard, and two project/manufacturing bridge modules.

**Consequence for the session:** the author-chosen list was a proxy for the population and was wrong by 5 members — the exact defect the project denominator rule exists to prevent. The Layer 1 registers use the 9-module denominator, not the 13-name list. Class of the 9-module figure: **A within the stated pattern and root set**; the pattern's false-negative mode (instantiation through a variable-held model name) is declared and **not** searched — class **C** for that residue.

### COR-P09-02 — Purchase, sales, expense and asset modules are **not** analytic-line producers. (Corrects an implicit premise of E00 §0.3 and of two briefs.)
None of the four instantiates an analytic line. Each only *stages* a distribution on a document that later becomes a journal item; the line is then produced by the ledger layer at posting. E00's P1 population is a population of **distribution carriers**, and this correction fixes the reading that a carrier is a producer. They are two different populations and E00 §0.3 must not be read as one.
Class **A** (direct-instantiation pattern over both roots, non-test files).

### COR-P09-03 — The analytic plan model has **no company field at all**. (Strengthens and partly restates E00-028.)
E00-028 recorded that the plan model has no record rule. The stronger fact is that the plan model carries **no company field whatsoever**: plans are global objects by construction, and the record rule is absent because there is nothing to scope on. Per-company behaviour exists only on the *applicability* child record and on a company-dependent default.
Class **A** (plan model read in full, 355 lines, by two independent readers).
**This is the single most important tenant-boundary fact produced by the session.** The dimension *structure* of management accounting is not tenant-scoped; only the dimension *values* and the *obligation to use them* are.

### COR-P09-04 — The maintenance surface has **zero** analytic references, in Python and in XML.
E00 carried no claim here. The tasked researcher enumerated the four maintenance-family modules and ran a combined analytic/accounting pattern over both `.py` and `.xml`. Result: zero matches in all four modules on both file types. The equipment record carries a single bare float cost field with no currency, no company link, no analytic link, no journal link and no asset link.
Class **B** with a fully declared boundary (4 named modules, 2 file types, 1 combined pattern). Reported as *not found in that scope*, **not** as "does not exist".

### COR-P09-05 — The valuation-derived analytic line discards its ledger link even when a ledger entry exists.
The inventory-valuation producer, in its *real-time valuation* branch, reads the amount and quantity **from the posted journal entry's lines**, then writes an analytic line through a value builder that has no journal-item key at all. The link is therefore not merely optional here — it is **structurally discarded on a path where it was available**.
Class **A**. This is a materially stronger statement than E00-025 and supersedes any reading of E00-025 as "the link is absent only where no entry exists".

### COR-P09-06 — One custom analytic extension is present in two deployment copies and absent from the third.
The department-dimension custom module adds a department field to **both** the analytic account and the analytic line, plus a stored, related copy of the account's department onto the line. It is byte-identical in two of the three custom roots and **entirely absent** from the third. Two further equipment-related custom modules differ in real source content between those same roots, not merely in build artefacts.
Consequence: **whether the department dimension exists at all is a property of which copy is deployed, and that is unknown.** E00-002's class **D** is upheld and now has a named, material capability attached to it.

---

## PART B — EXTENSIONS

### B.1 — Changing analytic allocation on a posted entry (answers a mandatory P09 question)

**EV-P09-100 — The distribution field is absent from every posted-entry protection list.**
The ledger row exposes three named protection lists — a tax list, a fiscal list and a reconciliation list — consulted by the write guard. The distribution field appears in **none** of them. The guard therefore never invokes the fiscal lock-date check, the tax lock-date check, or the reconciliation check for a distribution-only write.
Class **A** (all three list literals read; guard body read).

**EV-P09-101 — The distribution field is absent from every integrity-hash field list.**
The inalterability hash is computed over a named field list per hash version. Across all supported versions the list contains at most description, debit, credit, account and partner. The distribution field is in none of them, so a distribution write on a hashed, chained entry does not break the chain and does not raise the hash guard.
Class **A** (all version branches read).

**EV-P09-102 — The distribution field is not tracked.**
The ledger row declares tracking on six fields. The distribution field is not among them, and the write path builds its tracking set from the tracking attribute, so a distribution change on a posted entry produces **no chatter entry, no tracking value, and no audit record**.
Class **A** (tracking declarations enumerated field by field; write-path tracking collection read).

**EV-P09-103 — On a posted row, writing the distribution unlinks and re-creates the analytic lines.**
The inverse method selects only rows whose parent entry is posted, unlinks their analytic lines, and re-creates them. Draft rows are a no-op on this path; their analytic lines are created at posting.
Class **A**.

**Combined answer to the mandatory question "can allocation change after posting?":**
**Yes — after posting, after the fiscal lock date, after the tax lock date, and on a hash-chained entry — with no audit trail.** The old analytic lines are destroyed and replaced. Nothing in the ledger changes. The only barrier found anywhere is a read-only attribute on **one** view (the invoice line's secondary tab); the journal-items list view, which is the accountant's normal working surface, carries no such attribute.
Class **A** for each component; the composite is stated as the conjunction of four class-A facts.

**EV-P09-104 — Resetting an entry to draft deletes its analytic lines.** The reset action explicitly unlinks the analytic lines of every affected row; posting re-creates them. Management history for that entry is therefore destroyed and rebuilt, not versioned.
Class **A**.

### B.2 — Residual and rounding behaviour

**EV-P09-105 — A residual is absorbed only when a plan's distribution completes exactly 100 %.**
The amount builder tracks a running total per root plan. When the running total reaches exactly 100 %, the completing entry is computed as the *remainder* of the balance rather than as its own percentage, so rounding residue lands on that entry. **When a plan never reaches 100 %, no compensating entry is created** and the residue is simply not allocated.
Class **A**. Read with E00-017 (no 100 % requirement outside mandatory plans), this means: an optional plan may be allocated to 60 %, and 40 % of the cost then exists in the ledger with no management representation at all — silently, with no reconciliation surface.

**EV-P09-106 — Zero-amount splits are dropped.** The line builder skips any split whose computed amount is zero at the row's currency precision. A 0.4 % allocation of a small balance therefore leaves no analytic line, while still counting toward the 100 % total.
Class **A**.

### B.3 — Propagation to derived ledger rows

**EV-P09-107 — Tax rows inherit the distribution conditionally.** A tax row inherits the base row's distribution only when the tax record carries an analytic flag **or** the repartition row is not used in tax closing; otherwise the distribution is forced empty. Distribution is additionally part of the tracked field set used to detect manual overrides during tax resynchronisation.
Class **A**.

**EV-P09-108 — Exchange-difference rows, bank write-off rows, early-payment-discount rows and automatic cut-off rows all propagate the distribution.** Each was located and read: the exchange-difference builder receives the distribution as a keyword and applies it to one of the two generated rows; the write-off builder copies it; the discount builder copies it to both the base and the derived tax portion; the cut-off and accrual wizard copies it, in one branch through a recomputed proportional dictionary.
Class **A** for each, with the caveat that the exchange-difference path applies the distribution to **one** of the two generated rows — the asymmetry is in source and is not commented.

### B.4 — Producers without a ledger

**EV-P09-110 — A timesheet *is* an analytic line.** The timesheet module does not define its own model; it extends the analytic line directly and post-processes it to write a money amount computed as negative quantity times an hourly cost, converted from the employee's currency to the company's currency at the line's own date. No journal entry is created or referenced anywhere in that module. Cost-object fields added at that layer: task, project, employee, department, manager, parent task, milestone.
Class **A**. **This is the canonical management-truth-without-financial-truth case and it ships enabled.**

**EV-P09-111 — A work-order writes analytic cost on every duration change.** The manufacturing bridge recomputes an analytic entry whenever the work-order duration is computed or set — not at order confirmation, not at posting. The value is negative hours times the work centre's hourly cost rate, distributed through the **work centre's own** distribution. Two further modules add a second, per-employee line and a third, project-attributed line from the same value. All three are unlinked on cancellation and on work-order deletion.
Class **A**. One business fact (an hour of machine time) therefore produces **up to three analytic lines** and zero journal items.

**EV-P09-112 — Work-in-progress has two unreconciled representations.** The ledger-side work-in-progress posting is an on-demand wizard that builds a plain entry and reverses it the next day; none of its row dictionaries carries a distribution, so it spawns no analytic line. The analytic-side work-in-progress proxy is the continuously updated per-work-order line set from EV-P09-111. The wizard computes its overhead by an independent cost calculation rather than by reading the analytic lines.
Class **A** for the two representations existing and being structurally distinct; class **B** for "not reconciled" (absence-of-code-path within the read scope of that module).

**EV-P09-113 — The platform reports on ledger-less analytic lines as a first-class case.** The project profitability layer contains a domain builder whose entire purpose is to select analytic lines whose journal-item link is empty, and its own source comment explains why a further condition cannot be added there. Ledger-less management data is therefore not an edge case in this design; it is a supported reporting population.
Class **A**.

### B.5 — Tenant boundary, extended

**EV-P09-114 — The privileged plan column is company-checked; the JSON distribution path structurally cannot be.**
Two linkage mechanisms exist and are unequally protected:
1. the fixed many2one column of the privileged plan carries an explicit company check and the model enables automatic company checking, so that path **is** protected;
2. the JSON distribution carries account ids inside a JSON value. A company check is a many2one mechanism; it cannot attach to a JSON payload. No substitute constraint was found: the analytic-line builder sets the new line's company from **the journal row's own company** and never compares it to the company of the accounts named inside the distribution.
Class **A** for (1); class **B** for the absence in (2), boundary declared as the ledger-row model and the analytic mixin, two named patterns.
**Consequence:** the protected path is the one dimension that is a many2one; the unprotected path is the one the current user interface actually uses.

**EV-P09-115 — Distribution-rule selectors match null as a wildcard on every field, not only company.** Each selector clause is "value or null", so a rule with a null partner, null category, null product and null company matches everything. The accounting layer adds three further selectors — an account prefix, a product and a product category — of which only the product carries a company check.
Class **A**.

**EV-P09-116 — Applicability is resolvable per company; the plan is not.** Because the applicability record carries a company and the plan does not, a plan can be mandatory in one company and optional or unavailable in another. The default is additionally company-dependent. This is the **only** per-company control on the analytic dimension structure, and it governs *obligation*, never *visibility* or *existence*.
Class **A**.

### B.6 — Equipment cost, extended

**EV-P09-117 — The only equipment-to-accounting bridge in the deployed custom set runs backwards, through the asset.**
A custom module extends the **asset** record with a many2one pointing at an equipment record, plus a related reference field, and overrides asset validation to write a status value back onto the equipment. There is no field on the equipment record pointing to an asset, an analytic account or a journal entry. The bridge is therefore asset→equipment, one-directional, and expressed as a status flip rather than as a cost relationship.
Class **A** within the custom roots read.

**EV-P09-118 — That same custom module carries dead code targeting a model that does not exist in the reference version.** A file in all three custom copies inherits a legacy model name that is absent from the reference tree; **no copy imports the file**, so it is present on disk and unloaded. A second file defining a standalone category model is likewise present and unimported in two of the three copies.
Class **A** (import lists read in all three copies; the legacy model name searched across the whole reference root and not found there — class **A** for that negative, scope declared).

**EV-P09-119 — Work-centre cost is the only machine-time-to-analytic path found.** Cost per hour is a plain float on the work centre in the base manufacturing module with no analytic linkage; the analytic bridge is added by the accounting bridge module, which makes the work centre itself a distribution carrier. Equipment and work centres are unrelated models in the reference tree — no field connects them.
Class **A** for the mechanism; class **B** for "no field connects them", boundary declared as the four maintenance modules plus the two manufacturing modules read.

**Answer to the mandatory question "how should non-Asset Equipment costs be tracked?":** the reference pattern offers **no** answer. Equipment carries an untyped scalar cost with no accounting or analytic connection; the only cost-bearing operational object that reaches analytic is the work centre, and it reaches it through its own master-data distribution, not through any equipment identity. Whatever SMEsPlus does here will be a **design decision without a reference precedent**, and is routed as such rather than as a gap to be closed by imitation.

---

## PART C — REVISED CANDIDATE LIST FOR ADVERSARIAL VERIFICATION

E00 routed five candidates. Two are upgraded, one is added.

| ID | Claim | Status after E01 |
|---|---|---|
| CH-CAND-01 | distribution-rule company constraint does not re-fire on a payload-only write | PLAUSIBLE (unchanged) |
| CH-CAND-02 | cross-company allocation reachable through a non-privileged plan column | **upgraded** — independently reproduced by a second reader (EV-P09-114); mechanism class A, operational consequence still unexecuted |
| CH-CAND-03 | postings arriving in an already-posted transfer period are never allocated | PLAUSIBLE (unchanged) |
| CH-CAND-04 | a partial analytic allocation is transferred at 100 % | PLAUSIBLE (unchanged) — highest severity |
| CH-CAND-05 | the shadow view multiplies rows per plan | PLAUSIBLE (unchanged) |
| CH-CAND-06 | **new** — a distribution write on a posted, lock-dated, hash-chained entry passes every guard and leaves no trace (EV-P09-100/101/102) | mechanism class A on three independent lists; composite routed for challenge |

**END OF E01.**
