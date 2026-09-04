# 18 — P04 REVISION LOG

Layer: **2 — audit quarantine**.

What this session corrected — in prior packages, in its own parallel research
streams, and in itself.

---

## 1. Corrections to prior packages

| ID | Prior statement | Correction | Evidence | Severity |
|----|-----------------|------------|----------|----------|
| **P04-REV-01** | The reference population is **797 modules** — stated in **21 files across two prior packages** (P2 and P3; P1 predates source access), once classified `FACT VERIFIED (negative)` | **797 entries · 791 directories · 790 installable modules.** The figure repeated as a population was a directory-listing entry count | Executed directly: listing, type-filtered find, manifest search | Low for conclusions, **High for method** — no negative finding changes, but a denominator repeated 21 times, and once classified FACT VERIFIED, was never executed |
| **P04-REV-02** | *"Two live mechanisms carry machine cost into product cost, and a third is proposed"* | **Nine distinct paths** under a declared enumeration unit (own rate field, own driver, or own destination ledger) | Rate-field and cost-computation sweep across the manufacturing, manufacturing-accounting, work-order and project modules | **High** — it widens the AAS+ veto's second limb |
| **P04-REV-03** | *"Depreciation already reaches production cost centres through the analytic distribution"* — named as one of two live mechanisms underpinning the veto | **It nets to zero.** Both lines of a depreciation entry carry the distribution; analytic-line creation applies no account-type filter; the amounts are computed from the signed balance and cancel | Traced the analytic-line creation path end to end | **High** — a control believed to exist does not |
| **P04-REV-04** | The custom asset-to-equipment module has **two** unimported model files (itself a correction of an earlier "one") | **Three** are unimported. Five of eight model files are imported | Full import-chain read | Low for function, Medium for code health |
| **P04-REV-05** | Company-optional master data across four object classes is a multi-tenant-safety failure | **Narrowed to one class.** A defect for the work centre, which creates a financial effect; **not** a defect for the machine register, which is legitimately tenant-scoped | Scope-aware analysis under the mid-session constitution correction | Reclassification — see `20` §4.1 |
| **P04-REV-06** | The upward-traversing visibility rule is a SaaS-security defect | **Re-classified.** Certainly a company-scope accounting-visibility defect; a tenant-security defect **only if** company hierarchies can span tenants — which P04 cannot determine | Record rules read directly; scope model applied | Reclassification — see `20` §4.2 |

## 2. Corrections this session made against itself

| ID | What happened | Why it is recorded |
|----|---------------|-------------------|
| **P04-REV-07** | A search-result summary asserted that a **30-day advance notice** to the assessment officer is required before writing off a fixed asset. Reading the underlying ruling in full showed it says the **opposite** on its facts — deduction was allowed **without** prior notice — and that the 30-day regime belongs to a **different instruction** whose scope names goods and scrap, not fixed assets | The false statement was one paragraph away from being written into a statutory register as FACT VERIFIED. It was caught by reading the source rather than the summary. The residual question is registered as `P04-B-24` **HOLD / EVIDENCE REQUIRED** rather than answered by inference |
| **P04-REV-08** | An early reading of the runtime capture suggested the whole live asset population originates from migration, on the strength of migration-namespace external identifiers | Reading the capture **script** showed its identifier query was restricted to a **hand-picked list of 26 names**. The result is not a population statement. Downgraded to `UNRESOLVED` and registered as `P04-B-02`. The safe inference — that the population was created by a path that attaches no asset model — is recorded separately and explicitly as **SUPPORTED INTERPRETATION**, with the three mechanisms that remain consistent with it named |
| **P04-REV-09** | Three parallel research streams in this session enumerated the **same** custom-addon population and returned **60**, **46** and **65**. One concluded *"no custom module touches the asset domain"* — a **false negative on a load-bearing question** | Settled by direct execution: **65 directories, two asset-touching modules, five file hits plus one manifest dependency**. Preserved in full at `05` §6 rather than silently corrected, because it is direct evidence for the standing lesson that independent verification is the only control that catches this class |
| **P04-REV-10** | An internal consistency check across the package found **five blocker identifiers referenced in one file and absent from the blocker register** — asset tagging and physical verification, component depreciation, third-party compensation, the received-not-billed recognition gap, and value-added tax on the sale of a fixed asset | They were registered as `10` §7A. The check itself is the point: a register that other files cite but do not populate is exactly how an open item stops appearing. The same defect this package documents across three prior packages (`08` §5) was present in its own first draft, and was caught by executing a cross-reference rather than reading the register |

## 3. Method rules this session enforced on itself

| Rule | How it was applied |
|------|--------------------|
| **A negative is scoped, never absolute** | Every "not found" in this package names its pattern and its path set. `13` §1.2 lists the ten negative patterns and what each negative means |
| **A denominator is executed, not quoted** | Two populations that had been carried by assertion were executed; both were wrong (`P04-REV-01`, `P04-REV-09`) |
| **A bounded query is not a population** | `P04-REV-08`. The bound is stated **at the point of use**, not only in the source register |
| **An explanatory manual is not a standard** | Every TAS 16 finding is classified as ACCOUNTING STANDARD INTERPRETATION. The gazetted text remains on hold (`P04-B-30`) |
| **A single ruling is not a general instruction** | `P04-LAW-D` is used for what it decides and not extended by analogy; the extension question is registered (`P04-B-24`) |
| **Cite the corrections, not the headline** | Prior packages were read for their contradiction, unresolved-evidence and adversarial sections, not their summary tables. That is how the handover residue in `08` §5 was found |
| **Preserve disagreement** | Four new expert disagreements are open in `15`; seven inherited ones are re-opened in `12` §3 |

## 4. Constitution correction applied mid-session

`SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction — was
received during execution.

| Requirement | How it was met |
|-------------|----------------|
| Do not reset, do not restart, do not discard evidence | The session continued. No file was re-derived. No prior evidence was discarded |
| Supersede blanket Tenant + Company enforcement | `20_P04_SCOPE_OWNERSHIP_MATRIX.md` produced, applying PLATFORM / TENANT / COMPANY to every material P04 object and operation |
| Revalidate **only** materially affected findings | Three were affected and are revalidated in `20` §4: company-optional master data, the upward-traversing visibility rule, and analytic distribution scope. `20` §4.4 lists what was reviewed and found unaffected |
| Record the required fields for each affected finding | Original finding → scope assumption used → why over-constrained → correct scope analysis → updated classification → architecture impact → cross-process impact → evidence required. Applied in `20` §4.1 and §4.2 |
| Update the registers | `12` §2.1 (`CTR-C-10` narrowed, visibly); `10` §7 (`P04-B-35`, `P04-B-28`); this log; `11` §6 and `20` §5 (peer dependencies) |
| Do not stop for peer processes | Eight peer dependencies opened; **none** stopped this session |
| Do not ask the Boss to select scope options | No question was put. Scope was resolved from business, legal and accounting semantics where possible, and placed on **HOLD — SCOPE EVIDENCE REQUIRED** where not (`P04-SC-01`, `P04-SC-02`) |

**One consequence worth stating.** The correction did not merely relax a rule —
it **sharpened** a finding. The prior company-optional finding covered four
object classes at High severity on a rule that no longer applies to all of them.
Narrowed to the work centre, it becomes a scope violation **on the correction's
own terms**: the object creates a financial effect and cannot answer which
company owns it, therefore DENY. Narrower, and harder to dismiss.
