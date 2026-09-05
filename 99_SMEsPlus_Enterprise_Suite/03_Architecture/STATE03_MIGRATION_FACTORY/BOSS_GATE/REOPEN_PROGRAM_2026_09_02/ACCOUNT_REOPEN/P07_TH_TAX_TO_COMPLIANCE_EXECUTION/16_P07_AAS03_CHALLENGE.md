# P07 — AAS-03 EXPERT CHALLENGE RECORD

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Challenge Design

Four experts, **disjoint assignments**, all adversarial, all read-only, all instructed to
read the primary source rather than the package's quotations, and all given the explicit
instruction: *"if any path in this brief is wrong, report it as a finding."* The briefs
were issued before the package was complete, so three reviewers worked against a moving
target and one of them recorded that fact unprompted.

| Expert | Assignment | Files under attack |
|---|---|---|
| `AAS-03/A` | VAT reporting and tax point | `02`, `04`, `07` |
| `AAS-03/B` | Withholding event model | `03` |
| `AAS-03/C` | Documents, chart, GL mapping, corrections, filing | `05`, `06`, `08` |
| `AAS-03/D` | **Method audit**: enumeration integrity, scope, dependencies, and a named negative-claim step | whole package, especially `13` and `20` |

`AAS-03/D`'s brief was deliberately aimed at the author's method rather than the author's
conclusions, because the programme's recorded pattern is that conclusions survive and
methods do not.

## 2. Verdict Summary

| | A | B | C | D | Total |
|---|---|---|---|---|---|
| `CONFIRMED` | 6 | 8 | 12 | 6 | 32 |
| `CONFIRMED but UNDERSTATED` | 1 | 3 | 4 | 2 | 10 |
| `OVERSTATED` | 2 | 2 | 3 | 1 | 8 |
| `REFUTED` | 1 | 1 | 3 | 2 | 7 |
| `NEW` | 8 | 8 | 8 | 7 | 31 |

**Seven claims by this session were refuted outright and eight were overstated.** All
fifteen were corrected in the body before publication; none was left standing with a
challenge attached.

## 3. Refutations — Claims This Session Got Wrong

| # | Claim as published in draft | Reviewer | What is actually true | Disposition |
|---|---|---|---|---|
| `R1` | `account.move.line.tax_period_date` is "read by nothing". | A | A reader exists: a readonly, `optional="hide"` list column. | Corrected in `04 §3`, `11 P07-N-02`, `20 §4`. Claim narrowed to "no report, compute, domain or SQL reads it". |
| `R2` | The four zero-rated and exempt VAT taxes have **no tax group**. | C, and independently A | They resolve at template load into `WHT 1%`, the first Thai group by id, whose settlement accounts are the withholding control accounts. | `P07-F-42` written; `06 §3A` added with the seven-step chain; `GL-02`, `G-02`, `G-03`, `G-05`, `G-06` all corrected. **The corrected finding is more serious than the original.** |
| `R3` | The Thai "Tax Invoice" wording is a hard-coded English literal. | C | It is a translated view term; `th.po` maps it to `ใบกำกับภาษี`. The statutory wording particular is **satisfied**. | Struck from `05 §2`; the surrounding finding now rests only on identity and issuance. |
| `R4` | "Every PND handler selects on tag membership." | C | Both **PND** handlers do; the third WHT report selects on certificate lines. The conclusion survives for a different reason. | `GL-01` reasoning corrected in `06 §3`. |
| `R5` | Form classification exists **solely** as the repartition tag text. | C | True for the two purchase families; for the income family it does not exist at all, because that family carries no tag. | `GL-05` corrected. |
| `R6` | The Thai return type has **no workflow configured** and **no deadline**. | C | Both are supplied by computation: the workflow resolves to the generic tax-report workflow and returns are auto-generated; a deadline is computed from a company-wide reminder day. | `08 §5.4` corrected. The replacement finding — a *generic* deadline presented as the statutory one — is sharper than the original. |
| `R7` | Population of tax-relevant modules = 15. | D | Not closed under this package's own declared dependency-closure pattern. Ten members missing, three of them materially tax-bearing. | `13 §5.1` added; corrected population = 25. |

## 4. Overstatements Corrected

| # | Overstatement | Reviewer | Correction |
|---|---|---|---|
| `O1` | The SMEsPlus registers are a **strict subset** of the vendor registers, "systematic and one-directional". | A | The unit differs, so subset is undefined at row level; the vendor path carries the same class of label dependency and can empty in the reverse direction; the SMEsPlus path imposes no tag predicate. Containment is a property of the **shipped configuration**, not of the predicates. `07 §5` rewritten. |
| `O2` | `V-I-03`: the zero reports repeat the move header tax amount on every line. | A | Numerically inert, because the row predicate pins that amount to zero. The **live** defect on the same SQL is base-side double counting via the tax relation join, which the draft did not state. `02 §5` corrected. |
| `O3` | No guard prevents both withholding frameworks acting on one payment. | B | A guard exists in the base application and **silently discards** the Thai line after the payment amount has been reduced. Worse, and of a different kind. `03 §6.1` rewritten; the reporting-layer limb survives. |
| `O4` | The "less withholding already posted" loop nets prior withholding. | B | Its sign means it can never subtract. A second partial payment re-withholds in full. `W-M-04` rewritten. |
| `O5` | "113 of 138" chart-template directories ship a fiscal position template. | D | Numerator counted **files**, denominator counted something else. Correct: **94 of 126**. The ratio had already propagated into the Layer-1 file. `12 §5` corrected; `19` corrected. |
| `O6` | Belgium sets the four deadline and workflow attributes. | C | Belgium's own VAT return type sets none of them either; it registers five returns and ships compliance-check templates. The comparison was rewritten around coverage and checks. |
| `O7` | The certificate carries a 16-value income-type selection. | C | Fifteen, counted entry by entry. |
| `O8` | `20 §5`: "record rules present for both" certificate models. | D | The line-level rule is a redirect to the parent, redundant, with a dead orphan limb. |

## 5. New Findings Contributed by the Challenge

Thirty-one new findings were raised. Those adopted into the register:

| From | Adopted as |
|---|---|
| A, C | `P07-F-01` **escalated** from a brittle-label dependency to a translation-mapping equality that empties both statutory registers on a Thai-language install — **the escalation stands; its stated trigger does not. `P07-F-72` refutes *"on a Thai-language install"* (Thai active in 4 of 5 identities, 1 carries the translation); the condition is install order. Record left as the challenge stated it.** |
| C, A | `P07-F-42` zero-rated and exempt VAT settling against withholding control accounts |
| A | `P07-F-41`, `P07-F-43`, `P07-F-44`, `P07-F-45` |
| B | `P07-F-51`, `P07-F-52`, `P07-F-53`, `P07-F-55`, `P07-F-56`, `P07-F-57`; `03 §7.1`, `§7.2`, `§7.3` |
| C | `P07-F-46`, `P07-F-47`; `A-15` widened from four to eight members |
| D | `P07-F-48`, `P07-F-49`, `P07-F-50`, `P07-F-54`; `13 §5.1`, `§5.2`, `§2.1` completion |

## 6. Where the Reviewers Confirmed the Package

Recorded because a challenge record that lists only failures is not a challenge record.

- **The central withholding claim survived intact**, verified independently in both of its
  exclusion mechanisms, and `AAS-03/B` judged it *under*-argued rather than over-argued.
- **`P07-F-34`** (transposed account descriptions) was called "the best-supported finding in
  the set" and confirmed in both languages from the primary data.
- **`13 §2`** reproduced exactly: all three manifest counts, both excluded-root counts, and
  all fifteen module paths. Two reviewers ran it independently. **No wrong path was found
  in the scope register.**
- **`P07-F-37`'s 118** reproduced exactly, with the peer-baseline method endorsed.
- **`07 §3`**, including the honestly published disproved column-shift hypothesis, was
  confirmed cell by cell.
- **The multi-tag duplication claim** in `07 §2` survived a hand-worked two-tag line.
- **No fabricated citation was found anywhere in the package** by any reviewer.
- **The Layer-1 file passed the vendor-token scrub with zero hits** on first run.

## 7. The Method Verdict, Recorded in Full

`AAS-03/D` reached a conclusion that this session accepts without qualification:

> The package's declared method is strong and, uniquely in this programme, partly
> self-executing. It fails in one consistent way: **declared patterns were not actually run
> to closure.**

Four instances, each a `PATTERN` or `UNIT` failure rather than a `PATH SET` failure:

1. The dependency-closure pattern was declared with "none known" false negatives and never
   run — costing ten population members (`R7`).
2. The undeclared-dependency check was run on one module and not on the population —
   missing the defect in the module that produces the PND returns (`P07-F-54`).
3. The restatement check was declared package-wide and evidenced against three files that
   did not exist — and when actually run, found four violations in the Layer-1 file.
4. The one new peer-baseline ratio switched unit mid-count (`O5`).

This matters more than any single finding. The `PATH SET` is the half of the Denominator
Completeness Rule that `13` spends its length proving, and it is the half that held. The
halves that failed are the ones the register asserted and did not demonstrate.

## 8. Reviewer Findings Not Adopted, With Reasons

| Item | Reviewer | Why not adopted |
|---|---|---|
| Claim that the tax-unit mechanism is broken for Thailand because Thailand ships no fiscal positions | author's own inference, tested during challenge | Refuted by the code's docstring: the mechanism creates its own fiscal positions and they carry no taxes. Recorded as discarded at `20 §8`. |
| Removal of `trl.refund_tax_id` from the migrated SQL treated as a grouping change | author's own draft | `refund_tax_id` is functionally dependent on a column already in the `GROUP BY`; not a defect. Never published. |
| Divergence between tax-group settlement accounts and repartition accounts treated as an inconsistency | author's own draft | The account descriptions state a deliberate two-stage design. Recorded at `03 §8` as inspected-and-coherent so it is not re-raised. |

## 9. Disposition Audit — Were the Claimed Corrections Actually Made?

Run after P11 tested the same question against its own challenge record and found **ten of
86 findings marked `ACCEPTED — CORRECTED` that were never edited into its registers**,
including that round's only `CRITICAL`. P04 supplied the rule — *a revision log is not a
correction; the edit is* — and both peers failed it. This file makes the same class of claim
about 15 corrections, so it was audited rather than trusted.

**Method, with controls, because P11's own audit failed first** on grep patterns whose
escaping silently did not match and returned "corrected" for four findings still present. A
positive control (a string known to be present) and a negative control (a string known to be
absent) were run before the checks; both behaved correctly, so a `MISS` here means absence
and not a broken pattern.

| Claim | Target file | Result |
|---|---|---|
| `R1` tax-period reader | `04`, `11` | present |
| `R2` `WHT 1%` resolution + §3A chain | `06` | present |
| `R3` translated literal | `05` | present |
| `R4` `GL-01` reasoning | `06` | present |
| `R5` `GL-05` income family | `06` | present |
| `R6` workflow computed | `08` | present |
| `R7` population 15 → 25 | `13` | present |
| `O1` subset rewritten | `07` | present |
| `O2` `V-I-03` | `02` | present |
| `O3` guard exists | `03` | present |
| `O4` `W-M-04` | `03` | present |
| `O5` ratio, **both** in the dependency register and the Layer-1 file | `12`, `19` | present |
| `O6` Belgium | `08` | present |
| `O7` 15-value | `05` | present |
| `O8` cert-line rule | `20` | present |

**Unrepaired claims: 0 of 18 checks across 15 corrections.**

This is stated without triumph. This package failed the *same rule* twice on the same day —
`REV-E-25` (runtime results written to a new file and a log while the two files that argue
those findings still read "not executed") and `REV-E-27` (an uncounted dump total). The
disposition column happens to be the one place it held, and it held because every correction
in this exchange was made as an in-place edit at the moment it was accepted, not batched for
later. That is the whole of the technique.
