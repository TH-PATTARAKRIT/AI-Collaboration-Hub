# 83 — P05 RESEARCH ERROR AND REVISION LOG — G01 PHASE S

`LAYER 2 — AUDIT QUARANTINE`
Continues `15`, `39` and `54`. **This file governs over any headline table in the G01 deliverables.**
Prior errors `RE-01`..`RE-30` are preserved in those files and are **not** restated here.

## 1. Errors Found in This Continuation

| ID | Claim as published | Error class | Corrected finding | Caught by | Affected |
|---|---|---|---|---|---|
| **`RE-31`** | `CI-01` (employee-reimbursement input) evidenced as **"993 rows on the v18 target"** | **Denominator / citation** — the total across all three funding routes was cited as one route's count | `own_account` = **2** · `company_account` = **357** · `petty_cash` = **634** · sum **993**. The three are **disjoint and exhaustive**. | **AAS-03 Expert 1** — from the document's own arithmetic, before any re-extraction | `69 §A` |
| **`RE-32`** | `CI-07` presented as a **seventh Candidate Input class** | **Category error** — it is a **cross-cutting property** any of `CI-01`/`CI-02`/`CI-04` may carry, with no distinct producer, data semantics or scope | Re-labelled; input count **7 → 6**; retained under its ID for lineage | **AAS-03 Expert 1** — noticed the table schema itself was non-conformant | `69 §A`, `§F` |
| **`RE-33`** | `69 §B` stated a blanket posting rule (*DR cost / CR obligation*) with no carve-out | **Implicit cross-domain decision** — a universal "always expense" rule silently encodes a **never-capitalise** decision, which is **P04's**, while `67 §4` simultaneously claims P05 has made no capitalisation determination | Carve-out added: the rule describes observed behaviour on the evidenced population and is **out of P05's authority** where an asset relation is asserted (`CH-08`) | **AAS-03 Expert 1** | `69 §B`, `67 §4` |
| **`RE-34`** | Candidate output payloads for attribution and re-invoicing omitted **company** | **Payload incompleteness** — every other COMPANY-scoped output carried it; without it the consumer must re-open P05's records, which is the failure a handoff exists to prevent | `company` added to `CO-03`, `CH-02`, `CH-06` | **AAS-03 Expert 3** | `69 §C`, `§D` |
| **`RE-35`** | `CO-04` withheld-tax payload omitted income-type/form classification, certificate identity, branch identifier and currency basis | **Payload incompleteness** — all four are documented in **this package's own evidence**; none required statutory research | Four fields added; the question of whether P05 *can* freeze them is routed to P07 as `CH-04a` | **AAS-03 Expert 3** | `69 §C` |
| **`RE-36`** | `ORPH-01` framed the correction gap as *"no correction event is published"* | **Understatement** — for a completed withholding certificate there is **no correction mechanism of any kind**, only deletion, itself blocked by a restrict constraint | `ORPH-01a` added; orphan count **4 → 5** | **AAS-03 Expert 3** | `69 §E` |
| **`RE-37`** | `67` applied a consistent rule on withholding-module ownership **without ever stating it** | **Undeclared boundary** — the boundary held in practice but was invisible to a reader | `DP-12` added, stating the rule explicitly: mechanics are readable, statute is not P05's | **AAS-03 Expert 3** | `67 §2` |

### From AAS-03 Expert 2 (Leadership Database Design)

| ID | Claim as published | Error class | Corrected finding | Affected |
|---|---|---|---|---|
| **`RE-39`** | `CI-02` (357) and `CI-03` (634) presented as a **clean partition** of the funding routes | **Partition asserted on one field, contradicted by another** | The partition is clean **on the typed funding field** and not across the record: **26 rows are typed business-funded while carrying a float-holder link**. Both counts stay correct on their stated basis; the funding route of those 26 becomes `C — NOT DECIDABLE`. **Recorded by no file in this package before now.** | `69 §A` |
| **`RE-40`** | Reimbursement-route claim behaviour described as evidenced | **Zero-instance basis not disclosed** | Both `own_account` rows are **unattached to any claim** (`sheet_id` null, 2 of 2). Every statement about reimbursement *claim* behaviour rests on source reading with **no observed instance** — untouched by the data, not confirmed by it. | `69 §A`, `§B` |
| **`RE-41`** | *"One obligation per claim on the reimbursement route; one per line on the business-funded route"* carried as a verified asymmetry | **Untestable prediction presented among verified counts** | Lines-per-claim is `{1: 979}` with **no exceptions**. Where claim and line are always 1:1 the two rules make **identical predictions**. Downgraded to `SUPPORTED INTERPRETATION`; it had been reading as `FACT VERIFIED` **by association with the true counts printed beside it**. | `69 §B` |
| **`RE-42`** | *"Payable lineage is severed"* | **Overstatement — correct grain, wrong reach** | Severed at the **line** grain (null table-wide, reproduced twice). The **claim-level** key survives on **712 of 712** entries and reconciles on amount for **711 of 712**, which reconstructs the link entirely on this deployment's one-line-per-claim shape. Narrowed, not withdrawn. | `69 §B`, `§E` |
| **`RE-43`** | `CO-05`, `CO-06`, `ORPH-02`, `ORPH-03` stated as negatives with **no A–E class letter and no boundary** | **Method rule violated by the author who wrote it** | All four re-stated with POPULATION, PATTERN, PATH SET, UNIT and a class letter. `ORPH-03` turns out to be class **E — not an evidence question at all**; recording it as an unmet evidence need would have been a second error. | `69 §C`, `§E` |
| **`RE-44`** | Two classification vocabularies run in parallel with **no mapping** | **Undeclared vocabulary collision** | Mapping table added. The gap is not cosmetic: it is **exactly the hole `RE-43`'s four negatives fell through** — a claim could satisfy the first vocabulary and silently escape the second. | `69` header |
| **`DUP-07`** | *(new item, not a correction)* | — | **11 groups / 23 rows** identical on (description, employee, amount, date). Both "duplicates" and "legitimate repeats" are overclaims on the available fields. **`C — NOT DECIDABLE`.** Not covered by `DUP-03`..`DUP-06`, which assert *"no detection control exists"* — a different claim from *"identical rows are present."* | `69 §E` |

### From AAS-03 Expert 4 (Lead Code & UI Architect)

| ID | Claim as published | Error class | Corrected finding | Affected |
|---|---|---|---|---|
| **`RE-45`** | `PSC-01`: *"In the reference these three collapse into one transition"* | **Self-contradiction inside one file** | **Two of three** collapse. Approval creates the entry in draft; **posting is a separate method, on a different state gate, behind a different permission group** — which the table *immediately above `PSC-01`* already said. Verified in source by the author. The defect is **relocated, not softened**: the conflated pair is the dangerous one. | `69 §B`, `70 §2`, `68 CQ-P05-03` |
| **`RE-46`** | The custom override was described as *"occurring 0 times / non-executing"* | **Understated mechanism** | It is **unreachable by construction**: it calls a parent hook that **does not exist in this generation** (grep across the whole core module returns nothing; the current hook has a different name *and* a different shape). It would raise, not no-op. | `45`, `69` |
| **`RE-47`** | The core module's version **MATCH** row | **Transform asserted, not sourced** | The only row whose two sides are not compared as written — one is derived from the other by a normalisation the table never sourced. Re-labelled **MATCH on a derived basis**; one class weaker than the five rows below it. | `68 §2` |
| **`RE-48`** | The declared PATH SET treated as complete; `MD-01` framed as a **single named exception** | **The fourth rung, again — a boundary declared and never proven** | **170 of 361 installed modules (47.1%) lie outside the declared path set.** Three inherit the P05 core models; one **overrides both methods `PSC-01` turns on**. `MD-01`'s finding survives; its framing does not. **`CQ-P05-13` re-opened.** | `13`, `68 §1`, `81` |

### Found by the author while executing Expert 4's test

| ID | Finding | Direction |
|---|---|---|
| **`RE-49`** | The installed-but-unread module provides a route in which a claim reaches **posted, and on the business-funded route paid, with no accounting entry created at all**. Measured rather than assumed: the qualifying flag is set on **0 of 993** rows, so the route is **latent, not live**, and it does **not** explain the 267 entry-less claims. | **Against the author's own new finding.** Stated at its weakest: installed, reachable by construction, **not observed firing.** |

## 2. Class Tally — this continuation

| Class | Count |
|---|---|
| Denominator / citation | 1 (`RE-31`) |
| Category error | 1 (`RE-32`) |
| Implicit cross-domain decision | 1 (`RE-33`) |
| Payload incompleteness | 2 (`RE-34`, `RE-35`) |
| Understatement | 2 (`RE-36`, `RE-46`) |
| Undeclared boundary | 2 (`RE-37`, `RE-44`) |
| Overstatement / unstated basis | 3 (`RE-40`, `RE-41`, `RE-42`) |
| Partition contradicted by a second field | 1 (`RE-39`) |
| Author's own method rule not applied | 1 (`RE-43`) |
| Self-contradiction within one file | 1 (`RE-45`) |
| Transform asserted, not sourced | 1 (`RE-47`) |
| **Boundary declared and never proven** | **1 (`RE-48`)** |
| **Arithmetic** | **0** |
| **Corrections originating from the author unprompted** | **0** |
| **Corrections originating from independent challenge** | **18** |

**Every count published in this package reproduced to the digit — twice, by two parties.** Not one
of the eighteen corrections is an arithmetic error. They are wrong predicates, unstated bases,
undeclared boundaries and one self-contradiction: the same distribution this programme has recorded
in every prior round, and the reason arithmetic checking is not a substitute for adversarial review.

### The one that matters most

`RE-48` is the fourth rung of the denominator rule — PATH SET — and it has now failed in this
programme repeatedly with the memory of the previous failures already written down. The path set was
**declared** in file `13` and treated as settled from that moment. **Testing it required no new
search**: the installed-module list and the declared roots were both already in hand, and the test is
an intersection of two sets the package had already published. It was never run because nothing
prompted it — until an expert ran one directory listing to check its neighbours.

> **A declared boundary reads exactly like a proven one.** That is the whole defect. The only
> control that separates them is a party who did not draw the boundary.

> **`RE-31` is the same defect class this programme has now hit twelve times: a denominator that was
> not the denominator of the claim.** It is notable that Expert 1 found it **without re-extracting
> anything** — the three counts in the document did not reconcile with each other, and that was
> visible on the page. The author published a table whose own arithmetic contradicted it.

## 3. Method Control Added

| Control | Origin |
|---|---|
| **Before publishing a set of sibling classes, check that their counts reconcile against a stated total.** If the classes are claimed disjoint, they must sum; if they are claimed exhaustive, they must sum to the population. A sibling set whose numbers do not add up is wrong on its face. | **`RE-31`** |
| **A candidate class must conform to the schema its siblings use.** If a row cannot be populated with the same fields as its peers, it is not a peer — it is a property, a boundary, or a different kind of thing. | **`RE-32`** |
| **A universal rule inside a bounded domain is a cross-domain decision in disguise.** Any "always"/"never" statement about accounting effect must carry the carve-out for the cases the package itself routes elsewhere. | **`RE-33`** |
| **A boundary applied consistently but never stated is not a declared boundary.** Write the rule down where a reader will look for it. | **`RE-37`** |
| **A declared PATH SET must be intersected with the deployed set before any negative rests on it.** The test is `installed ∩ declared`; it needs no new search and must be run in the round that declares the path set, not a later one. | **`RE-48`** |
| **When two counts share a population, check that a second field agrees with the field that defined them.** A partition proven on one column can be contradicted by another column on the same rows. | **`RE-39`** |
| **A claim whose two candidate rules make identical predictions on the available data is not verified by that data**, however many true counts sit beside it. State what the population *cannot* discriminate. | **`RE-41`** |
| **Every vocabulary a document uses must be mapped to every other vocabulary it uses.** An unmapped second vocabulary is where claims go to escape the first one's rules. | **`RE-44`** |
| **A negative stated at one grain must be tested at every other grain that could carry the same fact.** Severed at the line does not mean severed at the document. | **`RE-42`** |

## 4. Preservation

Every corrected claim remains in place with its original text struck through or explicitly quoted.
Nothing was silently rewritten. Commit `47b714c` carries `RE-31`/`RE-32` in its message; `RE-33`..
`RE-37` are carried by the commit that follows this file.
