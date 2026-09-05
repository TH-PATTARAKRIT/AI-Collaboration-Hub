# P08_EXPERT_CHALLENGE_CORRECTIONS

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T14` part 1 of 2

Corrections to **published P08 findings**, raised by independent AAS-03 challenge and **re-verified by the author against the primary evidence before adoption**. `Independent Review ≠ Truth. Verified Evidence = Truth Basis.`

Every correction below was re-run by the author. **Every figure the reviewers reported reproduced exactly.** Where a reviewer's *reasoning* goes further than their *measurement*, this file adopts the measurement and says where it stops.

**Scope of this file: Experts 1 (functional accounting) and 3 (integration and localization).** Experts 2 and 4 were still running when this file was opened; their dispositions are recorded in `48`.

---

## 1. `P08-CORR-01` — the orphan-entry finding was over-claimed by **8.6×**, and it contradicted another file in the same package

**Published (file 38):** *83,820 plain journal entries have no link to any originating object* — read as roughly half of all posted entries.

**Re-run by the author. The reviewer is right, and the defect is worse than a miscount: it is an internal contradiction.**

The link set used was `payment_id`, `statement_line_id`, `tax_cash_basis_origin_move_id`, `auto_post_origin_id`, `reversed_entry_id`, `invoice_origin`. **It omits the two entry-level origin pointers that are populated at scale.**

| Re-run on `DB-SM`, posted entries of type *entry* | Count |
|---|---|
| Orphans under the published link set | **83,820** *(reproduced exactly)* |
| — carrying an inventory-valuation origin pointer | 56,559 |
| — carrying an asset origin pointer | 17,507 |
| — **carrying either** | **74,066 — 88.4%** |
| **Residual with no pointer of any kind** | **9,754 — 5.8% of posted entries, not 49.6%** |
| — of which no reference text either | **5,786** *(the published figure; it was correct and attached to the wrong parent)* |
| The auto-post pointer, included in the link set | populated on **0** entries — a **dead predicate** that made the negative look better supported |

**`file 38` and `file 41` contradicted each other on the same database in the same session.** File 41 §4 classifies 113,231 items as inventory valuation and 60,079 as asset depreciation, both *"reliable — entry pointer"*. File 38 counted those same entries as having no origin.

**`P08-CONTRA-22`. The headline is WITHDRAWN and restated: 9,754 posted entries — 5.8% — carry no origin pointer of any kind, of which 5,786 carry no reference text either.**

The corrected figure **does not** weaken the provenance finding in file 41, which was measured on a different and correct basis; it removes an inflated duplicate of it.

## 2. `P08-CORR-02` — "the 53 multi-line imbalances" is not the population the missing assertion would have caught

**Published (files 35 §4, 38 §3, 43 §6):** 1,851 posted entries carry a non-zero transaction-currency sum; the 1,798 single-foreign-line cases are exculpated as a denominated leg against a reporting-currency counter-leg; **"the 53 are the population the missing assertion would have caught."**

**Re-run. The reviewer's contradiction holds exactly.**

| The 53, re-run | Count |
|---|---|
| Carrying a **company-currency counter-leg** — the same shape already exculpated for the 1,798 | **49** |
| Every leg foreign and the memo still fails to sum — **the genuine residual** | **4** |

The four: a **0.04** rounding remainder across five legs, and three pairs of roughly **15–17** where one leg's memo amount is zero. **Aggregate economic significance is negligible.**

**The one-line-versus-two-lines cut is not an accounting distinction.** If one foreign leg against a company-currency counter-leg is legitimate, N foreign legs against a company-currency counter-leg is equally legitimate.

**`P08-CONTRA-23`. The sentence is WITHDRAWN.** The corrected statement: **4 posted entries, aggregate value negligible.** `AT-11` in file 38 and the reconciliation paragraph in file 43 §6 inherit this correction.

**This does not withdraw the mechanism finding.** It remains `FACT VERIFIED` that the balance assertion is scoped to the reporting currency only and that no layer enforces a transaction-currency invariant. What is withdrawn is the claim that the deployed data demonstrates material harm from it. **The mechanism is a real gap with an almost-empty measured consequence, and the package must say both.**

### 2A. Where the author does **not** follow the reviewer

Expert 1 argues from IAS 21 ¶21–23 that `KRN-INV-00` — zero-sum *in every currency frame* — would **refuse conforming entries**, because non-monetary items are held at historical rate and carry no meaningful current foreign amount. **The author finds the argument strong and the conclusion probably right**, and records the proposed split: an unconditional functional-currency zero-sum at the persistence layer, plus a separate **rate-consistency** invariant over monetary foreign legs only.

**But this is a standards question, and P08 does not settle standards questions from a reviewer's reading.** Recorded as **`P08-BD-18` — does the kernel's balance invariant bind per currency frame, or only in the functional currency with a separate rate-consistency rule over monetary items?** — `HOLD — AUTHORITATIVE ACCOUNTING-STANDARD EVIDENCE REQUIRED`, routed to the Accounting-Tax track and the Boss. **`KRN-INV-00` is marked `CONTESTED` and must not be inherited by any downstream design artefact until `P08-BD-18` is answered.**

## 3. `P08-CORR-03` — the backdating finding is 98.3% one automated catch-up run

**Published (files 35 §4A, 36 §3):** 6,418 posted entries carry an accounting date more than a year before creation; maximum 6,701 days — presented as *"the concrete form of the period finding."*

**Re-run. Every figure reproduces, and so does the signature the package never tested for.**

| The 6,418, characterised | Value |
|---|---|
| Asset-depreciation entries | **6,306 — 98.3%** |
| In a single journal | 6,281 |
| Created in **2024-01 / 02 / 03** | 6,270 |
| Largest same-second creation batches | **209, 192, 188, 186, 167** entries per second |
| **Non-depreciation residual** | **112** |

This is an **asset-register go-live catch-up**: a register loaded in early 2024 generating historical schedules for assets acquired back to 2005. The 6,701-day maximum is a 2005 asset, not an 18-year backdated posting. Batches of 200 entries per second are machine generation.

**Two defects follow, and the second is the author's.**

1. **The creation timestamp is a row stamp, not the posting act.** The package used it as *"the moment they were written"* and never tested for a bulk-generation signature — in a session that had already recorded `P08-M-06` about unexamined evidence bases.
2. The finding was headlined in **two** files. The hedge — *"P08 asserts nothing about whether any individual entry was improper"* — is accurate and is not what a reader takes from the table.

**`P08-CONTRA-24`. Restated: 112 non-depreciation entries backdated beyond a year, plus a 6,306-entry asset go-live catch-up.**

**And the restatement produces a better finding than the original.** A configured fiscal-year lock **would have blocked a legitimate migration**. That sharpens `P08-BD-16` rather than weakening it: the question is not only *refuse or relocate*, it is **what a close control does to a lawful bulk load** — and it is the strongest argument yet that the answer must be a business decision.

`P08-M-11` — **a population with a machine signature must be tested for one before it is read as human behaviour.**

## 4. `P08-CORR-04` — the retention control is **present** in the 19.0 deployments. The published claim was false.

**Published (files 35 §2, 36 §2, and repeated inside the correction file 40 §3):** *the retention column does not exist in any of the 3 databases — the feature is absent from the deployed version, so there is nothing to switch on.*

**Re-run against the extract headers. FALSE for 2 of 3.**

| Database | Column | Value |
|---|---|---|
| `DB-SM` (16.0) | **absent** | — |
| `DB-BK` (19.0) | **present** | **null on 44 of 44 companies** |
| `DB-EV` (19.0) | **present** | **null on 44 of 44 companies** |

The 18.0 source carries the same control under a different name. **The feature post-dates 16.0 and was renamed by 19.0. It was never absent from the estate.**

File 40 §3 posed exactly the right question — *absent because the feature post-dates 16.0, was renamed, or was never installed is `UNRESOLVED — EVIDENCE REQUIRED`* — **and left it unrun when the test was one grep of a header the session already held.** That is the `declared-pattern-not-run` defect, committed inside the file whose purpose was to correct version reasoning.

**`P08-CONTRA-25`. The claim is WITHDRAWN and ESCALATED, not softened: the retention control exists in the 19.0 deployments and is unset on 88 of 88 companies.**

**This strengthens the package's central structural finding.** The recurring pattern is *controls present in source and unengaged in deployment*. Retention had been the one apparent exception — a control genuinely missing rather than switched off. **It is not an exception. It is a sixth instance of the pattern.**

## 5. `P08-CORR-05` — the journal denominator is wrong in four files

**Published (files 35, 36, 38, 40 §2):** *0 of 64 journals have the tamper seal enabled.*

**Re-run. The count is 109.**

| Database | Journals | Seal enabled |
|---|---|---|
| `DB-SM` | 21 | 0 |
| `DB-BK` | **45** | 0 |
| `DB-EV` | **43** | 0 |
| **Total** | **109** | **0** |

The published 64 was `21 + 43` — **it recorded one database's count against the wrong database and dropped the third entirely.**

**The conclusion is unaffected and the evidence is stronger: 0 of 109.** But this is a denominator defect under a standing denominator-completeness discipline, in a session that raised that discipline twice. **`P08-CONTRA-26`. Corrected to 0 of 109 wherever it appears.**

## 6. `P08-CORR-06` — a new finding the package missed: the entry number is unrecoverable from **41.9%** of posted items

**Not previously in the package. Raised by Expert 1, re-run by the author, reproduced exactly.**

| Re-run on `DB-SM`, 447,384 items | Count |
|---|---|
| Items whose stored copy of the entry number differs from the entry's own | **174,977** |
| — **posted** items still carrying the draft placeholder while the entry carries a real number | **174,958** |
| **Share of the 417,700 posted items** | **41.89%** |
| Cancelled items retaining a different stale number | 18 |

**The general ledger, trial balance, balance sheet and profit-and-loss statement read the item table** — established by file 41 §7. **For 41.9% of posted items the sequentially assigned, legally significant identifier of the accounting record is not recoverable from the item at all.**

**This also corrects file 41 §2**, which published *"0 of 447,384 items disagree with their entry"* as `FACT VERIFIED`. The author re-ran it: the zero **holds** for the six provenance and context mirrors actually tested — and **fails for the entry number, which was not tested.** The claim was true of its test and stated as an absolute.

**`P08-CONTRA-27`. File 41 §2 restated: "0 disagree on the six mirrors tested"** — and the seventh, untested, disagrees on 174,977.

`P08-M-12` — **a mirror is not verified by testing some of its columns.** This is the same shape as `P08-M-07`: a claim that passed a control which did not cover it.

**Consequence for the source-of-truth model.** File 45 lists identity among the dimensions where the item is weak. This measurement makes that concrete and worse: **the item cannot even name the entry it belongs to** for two fifths of the posted population, except by joining.

---

## 7. Adopted with a stated boundary, not re-verified in full

| Reviewer finding | Author disposition |
|---|---|
| **E1**: the item's date, journal, company, reporting currency, number and posting state are all **stored mirrors of the entry**; seal, reversal lineage and the balance invariant are entry-level only | **ADOPTED.** The author verified the balance assertion is entry-scoped and the seal fields are entry-level. The full mirror list is reviewer-supplied. **It materially changes file 45's answer** — see §8 |
| **E1**: file 41 §8's design requirement (carry provenance on the item) **contradicts** file 41 §2 (item-level mirrors add no information) | **ACCEPTED as a real internal contradiction.** `P08-CONTRA-28`. The author does **not** adopt the reviewer's preferred resolution — "the fix is a join, not a duplication" is a design position and belongs to P11 |
| **E1**: file 34 §5's *"17 of 19"* is unsupported; the true remainder is 4, including two claims absent from the re-run entirely | **ACCEPTED PENDING RECOUNT.** Expert 4 was commissioned on exactly this and had not returned; disposition deferred to `48` rather than settled twice |
| **E1**: the root set is **14 roots on one product line and 8 on another**, and three roots are **nested inside** others, so *"0 in 21 of 21"* is not 21 independent observations | **ACCEPTED, MATERIAL.** This is `P08-M-08` unapplied to the session's own principal deliverable. Deferred to `48` with the recount |
| **E3**: the custom register source read is an **uncommitted working copy at 18.0** while the deployed module is at **16.0** — but the pre-migration revision carries the **identical predicate**, so the mechanism claim survives | **ADOPTED.** The evidence did not support the conclusion; the conclusion happens to hold. Recorded as a method defect, not a withdrawn finding |
| **E3**: 4 of the 5 excluded tax groups are **withholding** groups, not VAT rates; and the zero-rated and exempt VAT taxes are excluded by a different route entirely | **ADOPTED.** File 42's *"any rate that is not 7% is silently outside the statutory register"* reads as suppressed VAT and is **mischaracterised**. `P08-CONTRA-29`. **All statutory readings remain `HOLD — STATUTORY EVIDENCE REQUIRED`** |
| **E3**: **two disjoint Thai VAT reporting stacks** exist — the custom one in `DB-SM`, the vendor one plus an extension in `DB-BK`/`DB-EV`; the extension exists in **neither source tree** and in **zero** package files | **ADOPTED, MATERIAL.** The sweep examined one stack and generalised. `C NOT YET SEARCHED` for the second |
| **E3**: **33 of 65** custom modules are installed in at least one database, not 9; and **32 modules installed in `DB-SM` exist in neither source tree**, including two touching entry numbering and one touching translation — the two mechanisms under the numbering and tax-group claims | **ADOPTED, and this is the most consequential intake item of the four experts so far.** File 42's *"the most severe code findings are largely not deployed"* **does not inherit** file 40's `C NOT YET SEARCHED`, which was written four minutes earlier. `P08-U-18` |
| **E3**: the gapless-counter claim **fuses a design fact with a configuration fact** — the field was retired in the source line studied and is the live mechanism in the deployed line | **ADOPTED.** `P08-CONTRA-30`. The measurement stands; the fusion does not |
| **E3**: 16.0 carries **three** lock dates, the 19.0 databases carry **five** and not the same three; file 36 states five and was never re-scoped after file 40 | **ADOPTED.** The measurement — **0 set across 89 companies** — is unaffected |
| **E3**: the package's own quarantined evidence records a **statutory register query with no company predicate**, in a module installed on two 44-company databases, and it appears in **none** of files 33–47 | **ADOPTED, MATERIAL.** The closure did not carry its own strongest localization evidence forward. `P08-U-19` |
| **E3**: only the bank-statement boundary was tested in deployment; the payment-provider and electronic-invoicing tables are **not in the extract set at all**, and the electronic-invoicing module — a load-bearing counterexample in the `RS-A-01` withdrawal — is **uninstalled in both 19.0 databases** | **ADOPTED.** File 39 §4's heading over-states its own coverage. The withdrawal of `RS-A-01` **stands** — the author verified three counterexamples directly against source — but its deployed-relevance claim narrows |

## 8. What these corrections do to the package's central answer

**They do not overturn it. They sharpen it in one direction: away from the item.**

File 45 answered the mandated question in three parts — the item is the source of truth for monetary fact; meaning is split; event identity is absent as a platform property. **Corrections 01 and 06 both push against the item's standing**, and E1's mirror analysis pushes hardest:

> The item owns **amount, account and party**. The **entry** owns date, posting state, number, seal, reversal lineage — and the balance invariant itself is computed by grouping items **by entry**.

**The revised answer, which the author adopts:** the atomic unit of accounting truth in the benchmark is **the entry together with its item set** — not the item alone. The item is the *measurement decomposition* of the entry. File 45's first row is corrected from *"the journal item is the source of truth for monetary fact"* to:

> **The item is the sole store of the monetary decomposition. The entry is the sole store of everything that makes that decomposition an accounting record — when it is recognised, under what number, whether it is final, and whether it has been corrected.** Neither is the source of truth alone.

Whether SMEsPlus's kernel should therefore attach finality, numbering, sealing and dating to the **entry-equivalent** rather than the **item-equivalent** is a **`DESIGN CANDIDATE`, and it is P11's and the Boss's to decide.** P08 records that the benchmark, the accounting logic and two independent measurements — the 51% provenance figure and the 41.9% stale-number figure — all point the same way, and stops there.

---

## 9. Standing of this file

Nine published findings are corrected here; **six of the nine make the package's position weaker, and three make it stronger.** None was corrected silently: each carries a contradiction ID, and the withdrawn wording is quoted rather than replaced.

**The author's own record on this round: 0 of these 9 were self-caught.** Two independent experts, given the freedom to attack, found in one pass more material defects than the author's own three revalidation phases. That is the fourth time this programme has measured that ratio, and it is recorded again rather than treated as settled.
