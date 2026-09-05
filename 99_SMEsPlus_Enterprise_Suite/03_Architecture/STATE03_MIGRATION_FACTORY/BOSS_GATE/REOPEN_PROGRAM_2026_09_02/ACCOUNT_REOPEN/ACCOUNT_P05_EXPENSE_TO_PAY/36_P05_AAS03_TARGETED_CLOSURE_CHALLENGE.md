# 36 — P05 AAS-03 TARGETED CLOSURE CHALLENGE

`LAYER 2 — AUDIT QUARANTINE`
**This file and `39` govern over any headline table in the package (`ER-AASR-1`).**

## 1. Coverage — DISCLOSED SHORTFALL

The continuation directive required all four AAS-03 experts to challenge the closure results.
**That was not fully achieved on the first attempt, and the shortfall is reported rather than absorbed.**

| Expert | Role | First attempt | Re-dispatch |
|---|---|---|---|
| 1 | Leader Functional Design | **TERMINATED** — session rate limit (HTTP 429) | **COMPLETED on retry** |
| 2 | Leadership Database Design | **COMPLETED** | — |
| 3 | Lead Integration & Localization | **TERMINATED** — session rate limit | **COMPLETED on retry** |
| 4 | Lead Code & UI Architect | **TERMINATED** — session rate limit | status at publication in `35 U-14` |

**One of four completed on first attempt; three of four completed overall.** The three retries ran on
a smaller model than the originals, which is disclosed rather than glossed — their findings were
therefore all author-verified against source or data before adoption, and every one that could be
checked reproduced exactly.

This matters more than a scheduling note. The one challenge that did complete **contradicted two of
the three findings this continuation had published**. A round in which 25% independent coverage
overturns two of three headline results cannot claim that the remaining 75% would have found nothing.
**The coverage shortfall is itself evidence about the package's reliability**, and is carried into
`EC-02` and `EC-07` on that basis.

## 2. Design of the Challenge

Four disjoint mandates, each briefed to **disprove rather than confirm**, each carrying the standing
instruction *"if any path, figure or table cell in the artefacts is wrong, report it as a finding"*,
and each bound by the negative-claim classes, the prohibition on `PASS`/`FAIL` wording, and a
**read-only** constraint on the database evidence (never `-d`, never connect, never modify a dump).

| Expert | Mandate |
|---|---|
| 1 | Is the `U-01` module evidence sufficient for what is concluded from it? Is a convenience sample being treated as a population? Is a tolerance-zero downgrade on deployment evidence legitimate? |
| 2 | Does the database evidence actually prove the behaviour claimed? Re-derive every number; test the alternative explanations. |
| 3 | Are the WHT findings source behaviour or statutory conclusions? Is P05 overstepping P07? Verify `TX-01` from source. |
| 4 | Is the `CORR1` scope analysis correct? Is accounting lineage preserved? |

## 3. Expert 2 — Leadership Database Design — RESULT

**Every number the author published, Expert 2 reproduced exactly.** The arithmetic was sound. **Two
of the three interpretations were not**, and both were overturned.

| Claim | Verdict |
|---|---|
| `TX-13` — "32 payments hold multiple live statutory certificates" | **INTERPRETATION LARGELY REFUTED (class E).** 21 of 32 are one certificate per **distinct payee** on bulk payment runs — legitimate. 8 are same-payee **rate splits**. 2 are `done`+`draft`. **One** exact duplicate exists in 5,201. Overstated ~30×. The author's filter admitted `draft` and never grouped by supplier. |
| `TX-20` — "78.5% carry a date that is not the payment date" | **INTERPRETATION CONTRADICTED AND INVERTED (class E).** `payment_date == create_date::date` in **100.00%** of rows; the printed `date` matches the real payment date in **97.79%**. The author compared two columns and assumed which was the truth. |
| `TX-15` — 13 unreportable `pnd1` certificates | **CONFIRMED (class A).** |
| `TX-14` — class **D** hold | **Hold correct, reasoning incomplete** — a third explanation exists: the substitution FK is `ON DELETE SET NULL`, so deleting a predecessor silently erases the link. |
| `24` module matrix | **Reproduced cleanly** on the points tested. |

**Author response: both corrections accepted in full.** Every counter-measurement was independently
re-run by the author against the same data and reproduced exactly before adoption — per the standing
rule that a reviewer's disproof must itself be verified. `25 §3` was rewritten with the original
claims struck through, and the corrections propagated to `23`, `26`, `30`, `33`, `34` and `39`.

### Errors Expert 2 found in the continuation's artefacts

| # | Error | Disposition |
|---|---|---|
| 1 | `TX-20` mechanism inverted | corrected — `39 RE-10` |
| 2 | `TX-13` conflates one-certificate-per-payee with duplication | corrected — `39 RE-11` |
| 3 | **Denominator defect**: `25 §4` claimed "no v19 certificate population exists", omitting `BK12MAY26` — a registry the package had itself declared one file earlier, which holds 1 certificate | corrected — `39 RE-12`. **Second instance in this package of a negative contradicted by a root inside its own declared path set.** |
| 4 | The v16→v19 bracketing argument is thinner than presented — the model's relational shape changed between the two | corrected in `25 §4` |
| 5 | `25 §2` omitted material population caveats: 1,407 certificates (27.1%) have neither `payment_id` nor `move_id`; 1,417 have a NULL certificate number, 1,414 of them `done` | added to `25 §3` |

### New findings Expert 2 contributed — nine, all author-verified

`DB-01` no UNIQUE constraint on `payment_id` and no unique constraint of any kind ·
`DB-02` **no index at all** on the certificate table beyond its primary key ·
`DB-03` certificate lines orphaned by an `ON DELETE SET NULL` FK — **362 of 6,159 already orphaned** ·
`DB-04` no uniqueness on the certificate number — 75 shared, 1,417 NULL ·
`DB-05` declared payee disagrees with the payment's counterparty on **1,031 of 3,794** ·
`DB-06` **v16→v19 statutory-column regression** — `date`, `income_tax_form`, `supplier_partner_id` became nullable ·
`DB-07` v19 moves payment linkage to line level and adds PND1 payroll fields ·
`DB-08` derived-flag drift on 4 payments ·
`DB-09` a certificate line with `base=0, wt_percent=0, amount=72` that the schema accepts.

Full text at `25 §4b`. Expert 2's own assessment — *"DB-01/02/03/04/06 are new and, in my view, more
actionable than the two findings under challenge"* — is recorded and **not** argued with.

### A method defect Expert 2 exposed in the author's work

`pg_restore -s -t <table>` returns **only** the `CREATE TABLE`: constraints, indexes and FKs are
separately-named archive objects the `-t` filter excludes. Verified — the filtered extract yields
**0** matches for `CONSTRAINT|CREATE INDEX`. **A "no constraint exists" negative drawn from `-s -t`
is unfalsifiable by construction.** The author had used `-s -t`. Recorded as `39 RE-13`.

## 3b. Expert 1 — Leader Functional Design — RESULT

Re-dispatched after rate-limit termination; **completed**.

**On the data:** Expert 1 independently re-extracted `ir_module_module` from all six registries and
checked every cell of `24 §3` for the five decisive modules, plus the table-existence corroboration.
**Every value matched exactly.** It also verified from source that Odoo's module `state` has six
values, and confirmed as a checked negative that **no matrix module sits in `to install`,
`to upgrade`, `to remove` or `uninstallable`** in any registry — so the two-bucket legend, while
undeclared, corrupts nothing.

**On the conclusions: not sufficient as written.** Three errors, all accepted:

| # | Error | Disposition |
|---|---|---|
| 1 | **Unearned population claim.** The file wrote "**the** deployed estate" three times — a definite article asserting a population never established. The six registries are a convenience sample of files on one host; no search enumerated SMEsPlus deployments. | **Withdrawn.** `24 §4` correction; every §3 claim re-classed **A** for the six named files, **B** for anything wider. `39 RE-14`. |
| 2 | **`iTEST02` double-counted.** Two of the "five real business databases" are **one database sampled a month apart** — author-verified from the archive headers, both `dbname: iTEST02`. The name also signals a test/UAT environment (class **C**). So the `TZ-11`/`TZ-12` reach rests on **4 distinct databases, 2 distinct owners, one likely non-production** — not five independent corroborations. | **Corrected package-wide**, 7 files. `39 RE-15`. |
| 3 | State vocabulary collapsed without disclosure | boundary now stated in `24 §4` |

**And a substantive challenge to the register's central framing, which is accepted:**

> *"Deployment reach is close to the **wrong axis entirely** for a build-decision project… A confirmed
> design defect in code nobody currently runs is not **less** relevant — arguably it is **more**
> relevant, because it is a documented mistake SMEsPlus can still avoid inheriting."*

Expert 1 observed that `26 §5`'s "severity inversion" language **functions as a downgrade** for any
reader allocating effort, regardless of the `OPEN` labels beneath it — so the file was performing a
substantive reprioritisation while claiming only a formal one. **Accepted**: `26 §2` now carries the
challenge verbatim and `26 §5` is retitled and qualified. See `37 §3 NC+06`.

Expert 1 also noted the v18 sandbox does carry other SCGL custom code (`scgl_account_coa_control`),
softening the "not one custom module is present" framing.

## 3c. Expert 3 — Lead Integration & Localization — RESULT

Re-dispatched; **completed**.

**`TX-01` — CONFIRMED, and strengthened beyond the author's own citation.** Expert 3 read all four
source files independently and confirmed the inner join at `tax_report_pnd.py:57`, the `tax_tags`
engine on the on-screen report, and that neither the custom module nor core ever populates
`tax_line_id` on a write-off line. **The clinching detail the author had missed:**
`account_move_line.tax_line_id` is declared `related='tax_repartition_line_id.tax_id', store=True,
precompute=True` (`account/models/account_move_line.py:206-211`) — it is **not independently
settable**, and `tax_repartition_line_id` is never set on a write-off line either. **The NULL is
structurally guaranteed, not incidental — the finding is overdetermined.** Combined with the author's
production measurement (92.55% of 5,863 lines), `TX-01` is now the best-evidenced finding in the
package: predicted from source, proven inevitable by the ORM's field definition, and measured in a
production database.

**Statutory-leak audit — the package's discipline largely held.** A full read of `07` plus a keyword
sweep found **no hard statutory assertion**; every genuinely statutory question ends in
`HOLD — EVIDENCE REQUIRED`. Two defects were found and both are corrected:

| # | Defect | Disposition |
|---|---|---|
| 1 | **Soft statutory leak.** `TX-12` wrote "*a `done` — **potentially already-filed** — certificate…*". Nothing in source or data tracks filing status; this was an unsourced real-world assumption used to motivate HIGH severity, carrying no `HOLD` tag. | **Withdrawn** in `07 TX-12`. `39 RE-16`. |
| 2 | **P07 ownership overstep.** `30` `H-P07-2` labelled the per-payee certificate group "**(legitimate)**" in P05's own observation column — **pre-answering the exact question the adjacent column routes to P07**. | **Withdrawn** in `30 §3`. `39 RE-17`. |
| 3 | **Routing gap.** `BD-06`, `BD-07`, `BD-08` were posed directly to Boss with no P07 routing, though `BD-07` (who is subject to withholding) and `BD-08` (add-back scope) are Thai-statute territory. Boss would have been deciding P07's substance without P07 in the loop. | **All four `BD-05`..`BD-08` now carry explicit P07 / Accounting-Tax routing** (`07 §8`). |

Expert 3 declared its own boundaries honestly: it did **not** re-verify the ~60 other citations in
`TX-02`..`TX-24` or the non-P07 rows of `30` — class **D**, not executed.

## 3d. Expert 4 — Lead Code & UI Architect — RESULT

Re-dispatched; **completed**. Every citation it checked in `22`, `31`, `08` and `04` matched source
**verbatim** — across `petty_cash.py`, `account_withholding_tax.py`, `account.py`, `hr_expense.py`,
`hr_expense_sheet.py`, `account_move.py`, `fields.py`, `models.py`, `account_security.xml` and the
Thai WHT `security.xml`.

**One `CORR1` call overturned.**

| Finding | Verdict |
|---|---|
| `R-01` — `vendor_id` `check_company` withdrawal | **DOES NOT HOLD. Reinstated, narrowed.** `res.partner` carries its own optional `company_id` (`res_partner.py:294`), and Odoo core applies `check_company=True` to partner references precisely for this case (`account_move.py:372-380`) — so the *"reference scope ≠ financial scope"* argument was **contradicted by the platform's own design pattern**. Expert 4 also supplied the narrowing: `_check_company` runs inside `create()`/`write()` and **`sudo()` does not bypass it**, so the defect is **late failure**, not absence of a gate. This corrects `04 §4` in the opposite direction from the original finding. `39 RE-18`. |
| `R-02` — `petty.cash` COMPANY-scoped by derivation | **CONFIRMED, derivation sound.** Also confirmed the author's own earlier correction: the balance compute is not `sudo()`, so `account_move_line_comp_rule` does filter it; the genuinely unscoped defect is the `sudo()` lookup at `account_move.py:24,27`. |
| `R-03` / `SC-01` — WHT config over-constrained | **CONFIRMED (structural half; statutory half untouched per mandate).** Mechanism fully confirmed: the company-scoped `ir.rule` is what hides a same-tax record in another company and thereby **fabricates the duplicate**, while `default=lambda self: self.env.company` silently supplies the acting user's company. |
| `R-04` — approver via One2many | **CONFIRMED**, re-derivation accurate, not an overreach. |
| `R-05` — sheet `company_id` | **CONFIRMED**, correctly judged not over-constrained. |
| `R-06` — no-scope-assumption set | not independently re-derived (out of mandate); no contradiction found incidentally. |

**Accounting lineage — CONFIRMED, with a material omission the package never checked.**
Every severing citation matched verbatim. But a full-package grep for
`mail.message|chatter|tracking|ir.attachment|message_post|_creation_message` returned **zero hits
across all 39 files** — the package never asked whether lineage survives *outside* the foreign key.
It partly does: a permanent chatter message written at move creation, and receipt attachments
addressed directly to the move, both survive three of the four severing mechanisms (not the
draft-`unlink()` path, where `mail.thread.unlink()` removes the messages too). **Recorded as
`08 SR-07a`, bounding `SR-07`'s severity without overturning it** — chatter-parsing is not a
reconciliation key.

## 4. Coverage — final

**All four experts completed** — one on first attempt, three on retry after rate-limit termination.
`35 U-14` is closed.

The four rounds between them produced **four contradicted author findings** (`TX-13`, `TX-20`, the
population claim, the `R-01` withdrawal), **three withdrawn overstatements** (the "five databases"
count, the statutory leak at `TX-12`, the "(legitimate)" pre-answer at `H-P07-2`), **one accepted
challenge to a central framing** (reach is the wrong axis for a build decision), **one bound on a
headline finding** (`SR-07a`), and **one strengthening** (`TX-01` proven structurally overdetermined).
Nine new database-design findings. **Zero of these came from the author.**

## 5. `EC-07` Disqualifier Measurement for This Pass

| Disqualifier | Raised? | Evidence |
|---|---|---|
| New material population | **YES** | six module registries; 447,384 journal lines; 5,201 certificates — a class the package had asserted did not exist |
| New material finding class | **YES** | nine database-design findings; empirical confirmation as a class |
| New gating unknown | **YES** | `U-12`, `U-13`, `U-14` |
| Reopened tolerance-zero issue | NO | none reopened; reach reclassified, none closed |
| **New Gate-changing contradiction** | **YES** | `TX-13` and `TX-20` both contradicted — findings this continuation itself published |
| **Evidence-integrity failure** | **YES** | `RE-07` — the package asserted evidence did not exist when it did |

**Five of six disqualifiers raised. The pass is not clean. `EC-07` remains 0 of 2** (`29`).

## 6. What the Challenge Round Demonstrates

The original round's ratio was 12 of 32 author findings corrected by review, 60 new findings from
reviewers, 0 corrections originating from the author after review.

**This round is worse, on a smaller base:** of three findings the continuation published from new
evidence, **two were overturned by the first reviewer to look at them** — and that reviewer was one
of four. The author's self-check before publication caught none of them, despite having the same data.

The pattern across both rounds is consistent and worth stating plainly rather than leaving in a
table: **this package's author-produced conclusions have a high defect rate, and independent review
is the only control that has ever caught it.** That is the single most important input to the
`EC-02` disposition and to PMO's recommendation.
