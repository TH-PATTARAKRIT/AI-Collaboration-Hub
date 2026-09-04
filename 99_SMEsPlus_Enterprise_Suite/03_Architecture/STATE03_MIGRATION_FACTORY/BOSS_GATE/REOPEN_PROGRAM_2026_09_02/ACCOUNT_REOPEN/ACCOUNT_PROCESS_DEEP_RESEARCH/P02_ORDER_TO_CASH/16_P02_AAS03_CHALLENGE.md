# 16 — P02 AAS-03 INDEPENDENT CHALLENGE RECORD

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Standing Rule

`Independent Review != Truth. Verified Evidence = Truth Basis.`

**No challenge finding below was accepted on the panel's authority.** Every one that changed a package
statement was independently re-derived by the primary session from the same reference root before the
change was made. The verdict column records that verification, not the panel's confidence.

The four AAS-03 roles — Leader Functional Design, Leadership Database Design, Lead Integration &
Localization, Lead Code & UI Architect — were run as a single independent panel against the package, **not
against the reference**. The panel's brief was explicitly adversarial: *finding nothing is a failure of the
review, not a property of the package.*

## 1. Panel Findings — Verification Verdicts

### 1.1 Findings that CHANGED the package

| ID | Role | Finding | Primary-session verification | Package change |
|---|---|---|---|---|
| **CH-01** | Integration | **The Thai inbound-interim asymmetry does not exist.** The "Uninvoiced Receipts" account occurs **once in the whole localisation — in its own definition row** and is wired to no property. | **Re-derived and confirmed.** `EV-P02-081`; the Thai template assigns four property accounts and it is none of them (`EV-P02-043`). | **P02-F-05c and P02-F-38b WITHDRAWN.** Replaced by P02-F-38c (uniform absence). The symmetry premise routed to P01 in D-05 is withdrawn with them. |
| **CH-02** | Code/UI | **Owner-restricted stock does NOT produce a cost line on an order-linked invoice.** The re-derivation subtracts owner-excluded quantity before the top-up; the result is zero and the generator's zero-skip fires. | **Re-derived and confirmed.** `EV-P02-020`, `EV-P02-016`. | **One of P02-F-22's two instances REFUTED.** Edge case 7 reclassified from defect to sound. New `03` §5a. |
| **CH-03** | Code/UI | **The reset-to-draft guard exists and is wired on the purchase side only.** The link it tests is written in exactly one non-test place in the whole root. | **Re-derived and confirmed.** `EV-P02-092`, `EV-P02-086`. | New **P02-F-24b**. Collapses with P02-F-15 into one root cause. |
| **CH-04** | Code/UI | **The cost-of-sales expense fallback is the journal default account — and the chart sets a sale journal's default to the income account.** Cost of sales can be debited to Revenue. | **Re-derived and confirmed.** `EV-P02-090`, `EV-P02-091`. | New ledger row **AE-03b**; new row in `03` §5. |
| **CH-05** | Code/UI | **The unpicked-completion hole is reached via a MIXED picking, not an all-unpicked one** — validation force-sets the marker when nothing is picked. And the movement-level field **conceals** it after the fact. | **Re-derived and confirmed.** `EV-P02-087`, `EV-P02-088`, `EV-P02-089`. | **P02-F-16 reachability corrected; new P02-F-16b.** The finding is *sharper*, not weaker — one ordinary user action, invisible on the obvious field. |
| **CH-06** | Database | **The delivered-quantity field is a recomputed cache for goods, not a competing holder.** The compute assigns on every dependency change. The real second holder is the four methods with no outflow. | **Re-derived and confirmed.** `EV-P02-084`. | `05` §3a rewritten a **third** time; `01` §4 row 1 corrected. The finding narrows to services, expenses, milestones and timesheets — and points at a different question. |
| **CH-07** | Database | **The derivation-method selection has five values, not two.** | **Re-derived and confirmed.** `EV-P02-084`. | `05` §3a corrected. |
| **CH-08** | Code/UI | **The valuation-entry date has three branches; the package stated one and tagged it `FACT VERIFIED`.** | **Re-derived and confirmed.** `EV-P02-093`. | `06` AE-01 and `11` §5 corrected. |
| **CH-09** | Code/UI | **The lock relocation is capped at today and is not guaranteed to reach an open period.** With a future lock date it returns a date still inside the locked window, and nothing re-checks. | **Re-derived and confirmed**, including the reachability: the settings wizard refuses a future lock date, **the company-level write validation does not** (`EV-P02-082`, `EV-P02-083`). | New **P02-F-08b**; `11` §6 corrected. |
| **CH-10** | Integration | **The Thai statutory support export writes the accounting date into a column headed "Invoice Date".** | **Re-derived and confirmed.** `EV-P02-094`, `EV-P02-095`. | New **P02-F-51**. This is the sharpest Thai finding in the package and the primary session did not have it. |
| **CH-11** | Integration | **Four of the six Thai VAT taxes carry no tax group**, and the report counts tax exclusively from the 7% group. | **Re-derived and confirmed.** `EV-P02-096`. | New **P02-F-52**. |
| **CH-12** | Integration | **A sign defect in the Thai tax data** — the zero-rated input tax's refund repartition is positive where every sibling is negative. | **Re-derived and confirmed.** `EV-P02-097`. | New **P02-F-53**, routed to P01 and the Thailand tax process as a purchase-side item. |
| **CH-13** | Functional | **The obligation-ledger claim resolves fewer than six findings** — three of the six are one defect described three times, and three are untouched by it. | **Accepted on argument, not on evidence** — the reasoning is checkable against the package's own text and holds. | `10` §2a added; `17` D-I corrected; **D-VI split out**. H-01 handoff corrected. |
| **CH-14** | Functional | **The 37-case totals do not reproduce from the table.** | **Recounted mechanically and confirmed.** | `11` §9 totals corrected and the failure recorded as `RE-07`. |
| **CH-15** | Code/UI | **`03` §5 tagged idempotency `FACT VERIFIED` while §6 says it is deliberately not advanced.** | Confirmed by reading. | `03` §5 row split into two tags. |
| **CH-16** | Code/UI | **P02-F-15's headline is broader than its declared boundary** — the relation exists on the model; it is not populated. | **Re-derived and confirmed.** `EV-P02-085`. | P02-F-15 restated; collapses with CH-03. |
| **CH-17** | Code/UI | **"Double revenue blocked through the order path" is a default, not a block**; and **"double inventory relief blocked" is procedural, not a constraint** — the package applied a stricter standard to cost-of-sales than to inventory relief. | Confirmed by reading; the inconsistency is real. | `06` §4 both rows corrected. |
| **CH-18** | Database | **`20` declared no denominator** while making counted claims. | Confirmed. | `20` §0a added, declaring inheritance from T4 explicitly. |
| **CH-19** | Functional / cross | **The configuration premise — split recognition on, storable, real-time — is assumed in eleven files and declared in none.** | Confirmed. | `00` §3b added as a package-wide premise header. |
| **CH-20** | Cross-panel | **Index and count inconsistencies** — the Layer-1 filename in `00` §0, the register header range, and the handoff's evidence count. | Confirmed. | All three corrected. |

### 1.2 Findings ACCEPTED as gaps — coverage the package does not have

| ID | Role | Gap | Disposition |
|---|---|---|---|
| **CH-21** | Functional | **Drop-shipping is entirely absent** from the process map and the case matrix, and it has its own valuation path producing an **additional** journal entry (`EV-P02-099`). | **Accepted.** A first-class O2C shape with no case in this package. Recorded as a declared gap in `14` §2.4 and `15` §6. **Not closed** — closing it requires a new trace. |
| **CH-22** | Functional | **Credit control is absent** — the package walks Quotation → Close without asking whether the customer may be sold to at all. A customer credit limit exists (`EV-P02-098`). | **Accepted.** Recorded as a declared gap. It is a **pre-quotation** gate and would add an S0 to the spine. |
| **CH-23** | Functional | **Period-end unrealised FX revaluation of open receivables is absent** — the package covers realised difference at settlement only. | **Accepted.** For a Thai company invoicing in foreign currency this is the larger of the two FX effects, and it is an accounting event the 13-event register does not contain. |
| **CH-24** | Functional | Five further situations with no case: bill-and-hold; **outbound** consignment; warranty/return provision at point of sale; freight and delivery charges with their tax treatment; serial/lot-identified cost of sales. | **Accepted** as declared gaps. |
| **CH-25** | Integration | **The split-recognition toggle has no Community-equivalent interface** — it is exposed in one place in the whole root, in an Enterprise module (`EV-P02-101`). | **Accepted and verified.** Folded into `00` §3b. It materially changes what "the implementer must switch it on" costs. |
| **CH-26** | Integration | **The manual/periodic valuation default was asserted without a citation.** | **Accepted and supplied** — `EV-P02-100`. |

### 1.3 Findings NOT accepted, or accepted with qualification

| ID | Finding | Primary-session position |
|---|---|---|
| **CH-27** | `EV-P02-050`'s characterisation — "written, never read for duplicate prevention" — is wrong; the field **is** read, for a value-level duplicate control. | **Accepted in substance, and it strengthens the package's own point.** The reader nets already-posted cost quantity out of the re-derivation — that is duplicate control **at the value level, for one document's re-derivation**. It is **not** a guard against generating a second pair of lines, which is what `03` §6 claims is absent. The denominator (4 occurrences, complete) is reproduced by both parties. **`EV-P02-050`'s wording is corrected; the finding stands.** |
| **CH-28** | The withholding-certificate negative claim is tagged `VERIFIED ABSENCE` within the localisation but its boundary is stated as the whole root — two claims, one denominator. | **Accepted.** `06` §3 split into two claims with two boundaries. |
| **CH-29** | "791 module directories" does not reproduce as modules — 791 subdirectories, **790** carrying a manifest. | **Accepted.** Corrected in `14` §2.1. Trivial in isolation, material because the figure licenses a negative claim. |
| **CH-30** | `02` §3's matrix and §6's arithmetic assume a configuration the package's own headline says a Thai company lacks. | **Accepted** and answered package-wide by `00` §3b rather than file by file. |

## 2. What The Challenge Did Not Cover — Stated By The Panel Itself

The panel declared its own coverage limits, and they are **material to how much assurance this challenge
provides**:

1. **No runtime.** Every panel statement is static-source. The five runtime tests it specifies are the ones
   it could not run, and its reachability claims — CH-05's mixed picking and CH-09's future lock date —
   are read from control flow, **not observed**. Both were independently re-derived by the primary session
   from the same source, so they carry the same limitation.
2. **Roughly half the package's `FACT VERIFIED` markers were never examined.** The panel verified **no**
   citation in the T1 (return / credit / refund) or T2 (settlement / FX / deposits / write-off) evidence
   extracts. That means `08` in its entirety, `09` in its entirety, accounting events AE-05 through AE-13,
   and edge cases 18 through 30 are **unreviewed by this challenge**.
3. **T4 beyond two sections was not verified** — the intercompany, inter-warehouse, cross-company-leakage
   and year-end-closing sections stand unchallenged.
4. **The package was being written while it was being reviewed.** Six files changed under the panel
   mid-review; it re-read two and caught one silent correction. Findings against the four it did not re-read
   may address superseded text.
5. **The Thai statutory layer was not and could not be addressed** — the panel verified only what the code
   and the localisation data do.

**Point 2 is the one that bounds this challenge's value.** A review that examined half the evidence base
found twenty package-changing defects, two of which refuted the package's own findings. **There is no basis
for assuming the unexamined half is cleaner than the examined half**, and every conclusion drawn from `08`,
`09` and AE-05…AE-13 should be read as **once-verified, not twice-verified**.

## 3. What This Challenge Establishes About The Package's Method

| Observation | Evidence |
|---|---|
| Self-review found **six** corrections; independent review found **twenty** package-changing findings plus **six** coverage gaps. | `15` §3 versus §1 above |
| **Two of the twenty refuted findings the package had tagged `FACT VERIFIED`.** | CH-01, CH-02 |
| The package's own negative-claim discipline caught one defect before the challenge ran (`RE-06`), and missed two that the challenge caught (CH-01, CH-28). | `04` §11; CH-01, CH-28 |
| The single most inflated claim — "resolves six findings" — was **arithmetic on the package's own text** and survived every self-review pass. | CH-13 |
| The count in a summary table did not reproduce from the table beneath it. | CH-14 |

**`SUPPORTED INTERPRETATION`.** This reproduces the standing lesson exactly: **self-review finds a
fraction of what independent review finds, and the defects it misses are concentrated in headline claims
and summary counts rather than in the detailed evidence.** Nothing in this package's detailed citations was
found to be fabricated or misread; what failed was **aggregation** — counting, generalising, and stating a
finding more broadly than its own boundary licensed.

That has a direct consequence for EC-07: **one clean independent pass has now occurred and it was not
clean.** A second is required, and it must cover the half of the evidence base this one did not reach.
