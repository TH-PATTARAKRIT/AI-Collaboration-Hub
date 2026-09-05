# P01 — AAS+ CONSOLIDATION (SERIES-18 DIRECT VERIFICATION)

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-14`

AAS+ reconciles the run's own work with four independent challenges. **Dissent is preserved, not
resolved. Unresolved evidence is named, not absorbed.**

---

## 1. THE POSITION IN ONE PARAGRAPH

For the first time in five rounds, a P01 source finding and a deployed record are **the same
generation**. That is real and it is not small. But the round's most durable output is not the
accounting result — it is that **four adversarial challenges took eleven corrections off this
package in a single run, two of them falsifying claims the run had itself published hours earlier**,
and one of those falsified claims was a *bounded absence written in the same document as a section
correcting exactly that error class in someone else's work.*

**The accounting conclusions largely survived. The denominators, the reachability claims and the
evidence base did not.**

---

## 2. SAME-GENERATION SOURCE ↔ DEPLOYMENT PROOF

**Established, and it holds:**

- The deployment is series 18 — proved from the **schema**, and decisively by a string comparison:
  `ir_model_fields_selection` holds `manual_periodic`, which series 19 renamed to `periodic`.
  **A series-19 database cannot contain that string.** The database was **created** as series 18 on
  2026-08-18, with no migration residue anywhere; no series-14 code ever ran against these tables.
- The valuation policy is `manual_periodic` on **126 of 126** categories, read from **both** storage
  locations, with no product-level override possible in this generation. Attacked four ways by one
  expert and independently across all 504 (category, company) pairs by another. **It held every
  time**, and it is the single best-evidenced claim in the package.
- The receipt-to-GL gate is closed by that policy, and the consequence is measured.

**Not established, and now correctly framed:**

- Periodic is **sufficient but not identified**. A second writer exists that is gated on
  `cost_method`, not on valuation, and it was **reached and exercised** by 16 real price
  differences. **The zero on `account_move_line_id` is not explained by policy at all.**
- **A Python method override in a custom module leaves no database trace.** The scope of that gap is
  **56 non-core installed modules**, not the 16 this run first scoped.

---

## 3. POLICY-SENSITIVE ACCOUNTING SEMANTICS

**The central control of the round was observed, and it worked.** Two deployments show the same
zero; each was classified **independently** before comparison; the causes are opposite. Series 18:
policy is periodic, the journal is configured, the absence is correct. Series 19: the policy intends
posting and the journal is unset in every company. **SAME SHAPE / DIFFERENT CAUSE.**

**And the identification is stronger than the run first argued.** No stock location supplies a
valuation account (0 of 86, controlled), and 46,458 of 47,801 layers sit in fully-configured
categories — so a `real_time` counterfactual would have **produced entries**, not silent nulls. That
argument rules out *"it would have been zero anyway"*, and the run did not have it until an expert
supplied it.

**The scope is narrower than first published.** The verdict binds to 43,227 of 47,801 rows; 4,574
are over-determined; the runtime denominator is **541**, not 1,812; and only **61** layers are
purchase-linked.

---

## 4. GRNI / INTERIM ACCOUNTING

**Configured — strengthened.** 171 of 504 (category, company) pairs; **126 of 126** in the company
holding two-thirds of the ledger. The account is correctly typed, reconcilable, and named for its
purpose.

**Executed — no.** Zero items across the **whole three-account configuration** in four companies,
by three independent methods with a synthetic injection control. Inventory reaches the GL only
through migration journal 45.

**Reachable — the run's own "unreachable" was disproved.** Four writer routes, none needing a code
change. The sharpest is that `_check_valuation_accounts` **cannot refuse** a policy switch in
company 1, because all three accounts resolve on 126 of 126 categories — and one such write credits
account 176 in journal 40 for **฿29,835,023.51** of on-hand value.

> **AAS+ holds that this is the most consequential single sentence in the package**, and that it was
> only reached because an expert enumerated **writers** where the run had counted **rows**.

**And the unmeasured clause is named rather than glossed:** whether any user holds write access to
that field in company 1 has **not been measured**. Until it is, this is a **capability, not a live
exposure**. AAS+ specifically declines to let the well-evidenced half carry the unmeasured half.

---

## 5. POPULATION-SELECTION RELIABILITY — THE ROUND'S WORST RESULT

**Six instances of one shape, in one package.** A directory standing in for a population; a declared
root that excluded the deployment's own code; a name pattern standing in for a membership; a file
name standing in for a behaviour; a volume standing in for a host; a label standing in for content.

Three were found by the run. **Three were found by someone else**, and one of those falsified an
absence the run had published **in the same document as its own section on this error class**.

**AAS+ position: this is not a competence finding about any individual claim. It is a structural
finding about the method.** The programme has repeatedly diagnosed this defect correctly and then
committed it again in the next enumeration. `ERR-P01-24` records the sharpest form: the census
corrected in response to `ERR-P01-23` was **still directory-scoped**.

> **Writing the diagnosis feels like the repair, and it is not the repair.**

---

## 6. EXTRACTION RELIABILITY

**Better than the run claimed in one respect and worse in another.**

Better: every one of 59 COPY blocks reconciles; no artefact was truncated; the same table extracted
twice yields byte-identical data; the TOC reconciles to the archive header; `TABLE = TABLE DATA =
1,122` with zero materialized views.

Worse: **the run's own count of its false zeros was 1 where the artefacts show 4**, and the
discriminator that would have caught all four — a 718-byte shell versus an empty COPY block — was
available throughout, with seven natural positive controls sitting in the run's own outputs. And the
parser carries two latent defects that **cannot report their own failure**, both measured as not
having fired.

---

## 7. CROSS-GENERATION COMPARISON

Sound, and now carrying a migration exposure it did not have: **v19 drops the
`anglo_saxon_accounting` gate** on the bill-line override. In v18 that gate is FALSE in companies 2,
3 and 4, so the override **structurally cannot** fire there. In v19 the only remaining condition is
the valuation policy. **Stated as an exposure to be tested, not as a prediction.**

---

## 8. CROSS-PROCESS IMPLICATIONS

- **P08 / P11** — ฿29,029,467.66 tax-exclusive received-not-invoiced, unrecognised and unaccrued,
  of which ฿27,490,865.80 is receipt-backed; and 10 vendor bills whose liability sits outside the
  payables subledger.
- **P07** — the withholding attribution was **wrong** and is corrected; three statutory questions
  routed; **P01 answers none of them.**
- **P06** — `om_data_remove` is **installed here too**. P01 does not re-derive P06's finding and
  does not extend it; it reports the installation and hands it over.
- **P04** — two corrections adopted after verification; one reciprocal method contribution returned.

---

## 9. PRESERVED DISSENT

1. **Experts A and B on the discriminating set** — not reconciled away; they answer different
   questions and both corrections are carried (`P01_S18_AAS03_FRESH_CHALLENGE.md §5`).
2. **AAS+ against the run's own framing of the GRNI position.** The run repeatedly describes the
   unaccrued ฿29.03M as *"not a defect, a timing position"*. That is right about the software and
   **not sufficient about the accounts**: at a reporting date, an unrecognised and unaccrued
   received-not-invoiced position is a **completeness question**, and no periodic accrual exists in
   this database. AAS+ records that the framing leans toward reassurance and that **the judgement is
   P08's and the Boss's, not P01's** — which the package does say, and should say first.
3. **AAS+ against any reading of "the series-18 deployment".** Peer P04 identifies **three**
   series-18 identities and Expert D found a fourth artefact set. Everything here is bound to
   `551ab874`.

---

## 10. UNRESOLVED EVIDENCE — NAMED, NOT ABSORBED

| # | Unresolved | Why it cannot be closed here |
|---|---|---|
| 1 | Whether a custom module overrides a valuation **method** | No database artefact records a Python override; the gap spans 56 modules |
| 2 | Whether periodic was **chosen** or **lost in migration** | Needs a migration spec, a configuration decision record, or the predecessor's settings |
| 3 | Whether any user can **write** `property_valuation` in company 1 | Needs an ACL/rule resolution not run |
| 4 | Ten unenumerated database artefacts | Not read |
| 5 | Whether P01's series-16 withholding finding concerns this same OCA family | Needs the earlier round's **register and status field**, not its summary |
| 6 | The `remaining_qty` state at bill-posting time on 16 layers | Undecidable from one snapshot |
| 7 | Whether `om_data_remove` has ever run here | A raw `DELETE` leaves no trace |

---

## 11. AAS+ POSITION

**On the work:** the same-generation proof is real, the policy proof is the best-evidenced claim in
five rounds of P01, and the two-zeros distinction is a genuine and non-obvious result that would
have caused a material error in both directions had it been missed.

**On the package:** **do not rely on it yet.** Eleven corrections in one run, two of them
falsifications of same-run claims, is not a settled package. Every number that survived did so
because someone else checked it.

**On the method:** the four-way challenge with disproof assignments, a frozen brief, and one expert
scoped at the evidence base is the highest-yield control this programme has run. **It should be the
default, not the exception.** The three defects the run found in itself and the three found by
others is the ratio that matters: **self-review is necessary and it is not sufficient.**

**AAS+ raises no veto.** The corrections are absorbed, the dissent is preserved, and the open items
are named. **The exit position is unchanged, and §11 of the P11 supplement says why that is the
honest report rather than a disappointing one.**
