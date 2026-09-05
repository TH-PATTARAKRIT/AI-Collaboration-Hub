# P01 — AAS-03 TARGETED EXPERT CHALLENGE

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Expert reports are Layer 2 working material in `_expert_out2/`.

Four experts, **disjoint assignments**, three of them carrying a mandatory **disproof** task.
Every finding admitted below was **re-derived by this session** unless explicitly labelled
*expert-reported*.

---

## 1. THE THREE DISPROOF VERDICTS

| Claim put up to be broken | Verdict |
|---|---|
| *"The receipt-to-bill liability bridge does not exist in the deployed v19 population"* | **CLAIM REFINED** — wrong in scope, under-stated in mechanism, over-stated in population |
| *"Posted bill correction destroys accounting lineage"* | **CLAIM REFINED; strong form CONTRADICTED** |
| *"WHT compounds on partial vendor payments"* | **CONTRADICTED as stated** — the mechanism cannot fire |

**Three of three disproof assignments landed.** Not one of the three claims survived unchanged,
and two were substantially wrong. This is the strongest argument in the P01 programme for the
disproof format over ordinary review.

---

## 2. WHAT THE CHALLENGE DID TO THIS SESSION'S OWN WORK

| # | This session held | What an expert did to it |
|---|---|---|
| 1 | Three databases readable, one not | **The fourth is readable** with a newer binary already installed on this machine. It is the **most relevant database in the estate** — the only one with three-way match, subcontracting and the requisition family installed, and the only one with any period lock set. `ERR-P01-15` |
| 2 | Two v19 deployments and one **v18** | **The third is generation 16.** There is **no readable deployed v18 database at all** — so the generation the source analysis targets has no deployed representative. Independently confirmed by two experts. `ERR-P01-09` |
| 3 | v19 has a receipt-side mechanism, merely unconfigured | **v19 removed the receipt-side bridge by design** — its perpetual option means *"Perpetual (at invoicing)"*, and the bill line posts straight to the valuation account. `ERR-P01-10` |
| 4 | Zero journal links across 14,441 movements proves receipts post nothing | **The relevant sub-population is two movements.** All 1,201 order-linked receipts come from inter-company transit; class **B**, not A. `ERR-P01-11` |
| 5 | Withholding compounds | **The offset term is inert** — it selects a balanced set and evaluates to 0.00 in 4,943 of 4,945 deployed payments. The real defect is **repeated full withholding**, linear not geometric. `ERR-P01-12` |
| 6 | The withholding module is installed everywhere, so the defect is live | **No deployed database runs that code** — the deployed version matches no copy in the declared path set. `ERR-P01-13` |
| 7 | At least one deployment misclassifies every certificate | **Neither mapping governs** — the dominant route is a wizard where the operator picks the form. `ERR-P01-14` |
| 8 | Three-way match, subcontracting and requisition are installed nowhere | **All three are installed** — in the excluded database |

**Eight corrections, every one from an independent expert.** In the previous round the ratio was
five self-caught to one externally caught. In this round it is **two self-caught to eight
externally caught** — and the two self-caught ones were both about *my own* reasoning, while all
eight external ones were about *the evidence base itself*.

---

## 3. WHAT THE EXPERTS FOUND THAT THIS SESSION HAD NOT LOOKED FOR

| Finding | Expert | Re-derived? |
|---|---|---|
| **No inventory value reaches the ledger by any route** — not at receipt (removed), not at invoicing (no account resolves), not periodically (closing disabled on 87 of 88 companies) | Functional Design | partially — the account counts, yes |
| The declared cross-company access guard **can never execute**, because the framework forces superuser mode and the deployed "create as" user is the superuser on **44 of 44** companies | Database Design | **yes** — verified |
| **Cross-tenant reachability is live today**: three unrelated corporate groups in one schema, and every company partner is selectable from every company | Database Design | partially — the module install state, yes |
| Deletion of posted journal items **does** write a durable audit record — but it is deletable, its field identification is null in every row, and the v16 deployment logs **zero** deletions | Database Design | no — expert-reported |
| Purchase-document dates are rewritten **in draft, with no lock involved**, on 19.6% of 39,758 documents | Code & UI | no — expert-reported |
| Landed cost: **installed in all four, exercised in none**, and unusable on 43 of 44 companies | Functional Design | partially |
| Only **one** of 90 company rows has any lock date set | Code & UI | no — expert-reported |

---

## 4. WHERE EXPERTS CORRECTED THEMSELVES

Recorded because it is evidence of method quality, not decoration.

- The Code & UI expert first attributed the draft date-rewrites to lock enforcement, **found that
  wrong, and corrected it before publishing**.
- The Functional Design expert corrected three of this session's figures *and* its own brief's
  phrasing about test-file occurrences.
- The Database Design expert corrected an earlier pattern that missed a rule form, and another
  that missed inline constraints — **either would have produced a false verified-absence**.

---

## 5. WHERE THIS SESSION CORRECTED AN EXPERT

| Expert claim | Correction |
|---|---|
| The company-level stock journal is unset *"against a `NOT NULL` column"* | **The column is nullable.** The unset count (0 of 44) is right; the constraint characterisation is wrong |
| *"No runtime use anywhere"* of the clearing accounts in v19 | **15 occurrences exist in test files** — the expert itself flagged this against the brief's phrasing, and it is recorded here as the corrected form |

---

## 6. DISSENT PRESERVED

| Subject | Positions | Resolution |
|---|---|---|
| Whether the v19 receipt absence is design or misconfiguration | Functional Design: **design** — the bridge was deleted. This session earlier: misconfiguration | **Expert governs; verified.** Both are partly true — the design removed the receipt route, *and* the invoicing route is unconfigured |
| Subcontract credit split | **FACT VERIFIED for v18; CONTRADICTED for v19** | Both retained, version-bound. A correction is owed to P03 |
| P05's withholding rating | This session challenged it; the expert found P05 had already superseded its own summary | **`BOTH PARTIAL`** — no peer overruled |

---

## 7. WHAT THE CHALLENGE DID **NOT** COVER

- No expert executed a transaction. **Nothing in this package is runtime-verified.**
- `D4`'s transaction data was **not** analysed — only its module registry.
- Several expert findings above are **expert-reported and not re-derived**; each is labelled.
- No statutory question was answered by anyone; all are routed to **P07**.
