# P07 — RESEARCH ERROR AND REVISION LOG

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Purpose

This log records every correction made **to this package's own claims during its own
execution**, and every governance change absorbed mid-session. It exists because the
programme's recorded pattern is that authors do not catch their own errors; publishing the
ones that were caught, and how, is the only way to tell a reader which controls actually
worked.

## 2. Governance Absorbed Mid-Session

| ID | Instrument | When | Effect on this package |
|---|---|---|---|
| `REV-G-01` | `SMEPLUS-DR-EXIT-8C-001` — Very Deep Research 8-Criteria Universal Exit Constitution, effective 2026-09-04 | Read during scope bounding, before any finding was written | `13_P07_SOURCE_LINK_REGISTER.md` was written to discharge `EC-01` before findings; `11 §5` was written to discharge `EC-06`; `18_P07_PMO.md` records the eight-criteria assessment; the terminal recommendation is bounded by `EC-07`, which this single first pass cannot satisfy. |
| `REV-G-02` | `SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction | Received **mid-authoring**, while `01_P07_THAI_TAX_REQUIREMENT_REGISTER.md` §7 was being written | Applied immediately without reset. See §3. |

## 3. Scope-Aware Correction — Delta Revalidation

Per the correction §6, only findings materially affected by the superseded
"Tenant + Company context everywhere" assumption were revalidated. All other evidence,
source links, contradictions and commit lineage were preserved unchanged.

| Original finding | Scope assumption used | Why it was over-constrained | Correct scope analysis | Updated classification | Architecture impact | Cross-process impact | Evidence required |
|---|---|---|---|---|---|---|---|
| `R-B-01` (as first drafted): "Tax master data must belong to exactly one company", assessed against `account.withholding.tax` | Blanket company ownership for all tax master data | The Thai rate and form catalogue is **national**, identical for every tenant and company. Requiring company context for it is an over-constraint that the canonical rule does not impose (`PLATFORM SCOPE -> company context NOT REQUIRED`). | The object holds **two** scopes in one record: a `PLATFORM` statutory reference (name, rate, form tags, type) and a `COMPANY` financial binding (`account_id`). One record cannot answer to two owners. | **Restated and strengthened** as a scope-conflation finding plus a separate unproven-ownership finding (`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`). `P07-F-18`. | The remedy is a scope split, not a company-id fix. A company-id fix alone would harden the wrong half. | `product.template.wt_tax_id` is a `TENANT`-scope reference into this object (`20 §4` row 10) and cannot be validated until the split is resolved. | none further; source evidence is sufficient |
| Implicit assumption that the statutory catalogue must be company-owned | same | The catalogue is a `PLATFORM` reference | Instantiating it per company is permitted; the correction does not require platform data to be physically singular | **New, downgraded finding** `P07-F-30`: over-instantiation, recorded as a scope-design observation rather than a defect — with the material consequence that one company-mutable label is used as a statutory report predicate | none on its own | none | none |
| Branch handling, previously framed only as a data-consistency defect | Blanket company context | It is a **scope collision**, not merely inconsistency: the counterparty branch is `TENANT`-scope master data and the filing branch is a `COMPANY`-scope legal attribute | Three representations across two scopes, used interchangeably; the `COMPANY`-scope attribute is read by no report | **Re-scoped** `P07-F-06`; new `R-B-04` | The filing-unit boundary required by `S-15` cannot be built on a counterparty attribute | `H-05` added to the P07 handoff contract | none further |
| Cross-company tax-unit grouping, previously unexamined | — | New question raised by the correction: unrelated independent companies are separate tenants by default | Whether the grouping is tenant-contained could not be established: no tenant construct was selected by the declared patterns in the P07 population | **New** `HOLD — SCOPE EVIDENCE REQUIRED`, `P07-U-14`; negative bounded as `P07-N-09` class `B` | unresolved | `P07-D-24` routed to P11 | tenant model evidence from outside the P07 population |
| External Revenue Department enrichment service, previously unexamined | — | New question raised by the correction §4 q.3–5 | Scope is `TENANT` writing tenant master data via a `PLATFORM` external service; the egress boundary was not assessed | **New** `P07-U-15`, class `C — NOT YET SEARCHED` | unresolved | none | egress and data-protection assessment |

New deliverable produced by the correction: `20_P07_SCOPE_OWNERSHIP_MATRIX.md`, answering
the eight correction questions for twenty material P07 objects.

Registers updated per correction §6: `11_P07_CONTRADICTION_REGISTER.md` (`P07-C-02`),
`12_P07_DEPENDENCY_REGISTER.md` (`P07-D-24`), this log, and the new scope matrix.
No research was re-run. No prior evidence was discarded.

## 4. Errors This Session Made and Corrected

Recorded in full, including the two that were self-inflicted, because a package that
reports only its findings and not its own defect rate is not auditable.

| ID | Error | How it was caught | Correction | Status at publication |
|---|---|---|---|---|
| `REV-E-01` | The draft of `03_P07_WHT_EVENT_MODEL.md` asserted "PND2 and PND54 appear nowhere". | By **running the declared pattern** (`pnd`, case-insensitive, all file types) instead of trusting the draft, as the negative-claim rule requires. | PND 54 **is** provisioned: `213303 Tax Withheld - PND 54`, with a bilingual description naming the remittance form. The claim was replaced by a four-layer provisioning matrix (`03 §4.1`) and a sharper finding: the chart names an obligation the reporting layer cannot serve (`W-K-07`). `P07-N-11` re-classed to `A` for the reporting layers and `E` for the chart layer. | corrected before publication |
| `REV-E-02` | The draft of `08_P07_CORRECTION_ADJUSTMENT_MATRIX.md` §5 asserted that **every** element of the filing/close segment was absent. | By checking whether a base filing framework existed before publishing a system-wide negative. | The base set contains `account.return`, `account.return.type` and `account.return.check` with deadline periodicity, days delay and workflow states, provisioned by 118 localisation modules. The negative was **withdrawn** (`P07-N-15`, class `E`) and replaced by a measured provisioning gap, `P07-F-37`. `01 §5 R-V-20` and `07 §4 T-04` were corrected in the same pass. | corrected before publication |
| `REV-E-03` | A column-shift defect was hypothesised in the SMEsPlus VAT report handlers (declared columns vs emitted columns). | By counting both sides for all four reports. | **No misalignment exists.** The hypothesis was wrong and is recorded as such at `07 §3`. What does exist is an asymmetry between the sale-zero and purchase-zero column sets (`P07-F-35`). The disproved hypothesis is published so a later reviewer does not repeat the check. | corrected before publication |
| `REV-E-04` | The first run of the fiscal-position enumeration used `-maxdepth 3` and returned **zero** results, which would have supported a false "no peer ships this either" reading. | By noticing that a known-good example (`l10n_be/data/template/account.fiscal.position-be.csv`) sat at depth 4 and could not have been matched. | Re-run at `-maxdepth 4`: **113 of 138** chart-template directories ship a fiscal position template, and Thailand ships none. The finding `P07-F-38` rests on the corrected run. | corrected before publication |
| `REV-E-05` | A draft observation treated the divergence between the tax groups' settlement accounts (`213500`, `114401`) and the repartition accounts (`213301`, `213302`, `114300`) as an inconsistency. | By reading the account descriptions, which state a deliberate two-stage design. | **Not a defect.** Recorded explicitly at `03 §7` as inspected-and-coherent so that a later reviewer does not re-raise it. What remains open is the executor of the consolidation, `P07-N-13` / `P07-U-17`. | corrected before publication |
| `REV-E-06` | A draft treated the removal of `trl.refund_tax_id` from the SMEsPlus tax-report SQL as a grouping change. | By checking functional dependency: `refund_tax_id` is an attribute of the same repartition-line row already in the `GROUP BY`, so removing it cannot change the grouping. | **Not a defect.** Not published as a finding. | not published |
| `REV-E-07` | An initial statutory retrieval indicated the 7% VAT rate expires 30 September 2026, twenty-six days after this session's date — which would have made `P07-F-01` an imminent compliance cliff. | By searching for a later instrument before publishing a dated risk. | A further extension to 30 September 2027 was approved by Cabinet on 27 July 2026 and confirmed by a Revenue Department notice on 2 August 2026. No finding asserts an imminent lapse; the structural coupling finding stands on its own terms. `P07-C-21`. | corrected before use |

| `REV-E-08` | On finding that the cross-company tax-unit mechanism synchronises fiscal positions, the session inferred that the mechanism must therefore be broken for Thailand, since Thailand ships no fiscal position templates (`P07-F-38`) — an attractive inference that would have linked two findings into one. | By reading the method rather than its name. | **Refuted by the code's own docstring**: the mechanism creates its own fiscal positions and those positions carry no taxes, so it does not depend on localisation templates at all. The inference was discarded and is recorded as discarded at `20 §8`. `P07-F-38` and `P07-F-39` are independent. | discarded before publication |

Seven of the eight were caught by mechanically executing a declared control — running the
pattern, counting both sides, checking for a later instrument, reading the method — rather
than by re-reading the draft. Re-reading the draft caught nothing in this session.

## 4A. Errors Found by Independent Challenge, Not by the Author

The eight errors in §4 were caught before publication by the session's own controls. The
following were **not** caught by the session and were found by the four AAS-03 experts.
They are listed separately because the distinction is the whole point of the control.

| ID | Error | Found by | Correction | Where |
|---|---|---|---|---|
| `REV-E-09` | "`tax_period_date` is read by nothing." | `AAS-03/A` | A reader exists — a hidden list column. Narrowed to "no report, compute, domain or SQL reads it". The author had **read that view file earlier in the session** and still wrote the absolute. | `04 §3`, `11 P07-N-02` |
| `REV-E-10` | Files `06` and `08` asserted system-wide negatives with no class and no boundary, while `02`, `03` and `05` registered theirs. | `AAS-03/C` | Negative-claim registers added to both. Of the negatives left unregistered, three were then found wrong or over-stated; **no registered negative has failed**. The correlation is recorded as evidence that the control does real work. | `06 §6`, `08 §6` |
| `REV-E-11` | The declared dependency-closure pattern was never run, so the population was understated by ten members — one of which the package simultaneously cited as evidence and registered as a broken dependency. | `AAS-03/D` | Population corrected 15 → 25. Recorded as a `PATTERN` failure, not a `PATH SET` failure. | `13 §5.1` |
| `REV-E-12` | The PND token census, offered as proof of a denominator, did not reproduce: it had been taken without the declared exclusions. | `AAS-03/B` | Corrected counts published beside the originals. Qualitative conclusions unchanged. | `13 §5.2` |
| `REV-E-13` | "113 of 138" — the numerator counted files and the denominator counted something else. The defective ratio had already reached the Layer-1 file. | `AAS-03/D` | Corrected to 94 of 126, with both commands published. This is a `UNIT` failure inside the very finding whose closing note congratulated this session for catching a `-maxdepth` error in the same enumeration. | `12 §5`, `19 §5` |
| `REV-E-14` | The restatement check was certified as executed while naming three files that did not exist, and excluding the files where restatement actually happens. | `AAS-03/D` | Check executed properly; four class-`B`-to-unqualified restatements found, **all in the Layer-1 file**, plus a count error. All corrected. The Layer-1 file had passed the vendor-token scrub cleanly on the same content — the two controls are independent. | `11 §5.1` |
| `REV-E-15` | Seven further substantive claims were refuted and eight overstated, including "no guard prevents both withholding frameworks acting on one payment" (a guard exists, and it silently discards), "the zero/exempt taxes have no tax group" (they resolve to a withholding group), and "the Thai tax-invoice wording is a hard-coded English literal" (it is translated). | all four | Each corrected in the body; none left standing with a challenge attached. | `16 §3`, `§4` |

| `REV-E-16` | The findings register's own totals were **asserted, never executed**: 49 issued against 48 actual, and every severity and evidence-state cell wrong. Then the first attempt to correct them re-derived the counts with a second pattern, double-counted a dual-state cell, and produced a total that summed correctly by coincidence — breaking the project rule *enumerate by call site, then read* inside the correction itself. | P04, by raising the identical defect against its own register and telling P07 to recompute | Totals enumerated row by row and republished with the asserted figures beside them at `00 §3.1`. | corrected after publication |
| `REV-E-17` | The Class 2 tally in the method proposal read "nine instances, nine actors": P04's figure was inherited uncorrected, four P07 instances were counted as four actors when they were one, and the same number was labelled on both axes — **a unit conflation inside a standard about counting**. | P04 | Recomputed with the unit declared: 12 instances across 5 actors, the two actor sets disjoint. The original sentence is preserved verbatim at `§3.1b` of the proposal. | corrected after publication |

| `REV-E-18` | `REV-E-09` was recorded as if the search had been too narrow. It was not: the grep **printed the reader** — `views/view_tax_period.xml:30`, a live field declaration — and the published conclusion contradicted the output the author was looking at. Re-executed to confirm the line was in the original output; it was. This is not a bounded-enumeration defect, it is **tool output standing in for the file it points at**. | P04, by referring a P11 case that has the same shape and proposing the class extension | Reclassified. The method proposal's Class 1 is extended to cover tool output at `r3`, evidenced on P07's own instance rather than on the referred one. | corrected after publication |
| `REV-E-19` | The sentence declaring the corrected Class 1 split wrote "3 P04, 2 P07" for a table containing 2 P04 and 3 P07 — a third counting error, in three consecutive revisions of the file whose subject is counting. | **the author**, by parsing the table instead of reading it | Corrected before publication. The only self-caught counting error of the exchange, and it required executing the count. | corrected before publication |

| `REV-E-20` | r2 and r3 published a single joint cross-party tally ("12 instances across 5 actors"). A cross-party tally **cannot be executed by either party** — P07 cannot open P04's drafts, P04 has not read P11's register. Every joint figure produced in the exchange was wrong. | P11, raising `P11-G-02` | Replaced by declared halves, each executed by its owner, with no total. P04's offer to restate it as "14 across 5" was **declined** — the halves were adopted, the single number was not, because producing one repeats the defect. Obligation 6 added. | corrected after publication |

Two of the reviewers' findings **escalated** the severity of the session's own headline
findings rather than reducing them (`P07-F-01`, `P07-F-42`), and both were reached
independently by two reviewers. The session's own severity assignment was too low in both
cases.

**Net for the round:** the author caught 8 errors in its own unpublished drafts; the
reviewers caught 15 in its published ones and contributed 31 new findings. Two further
errors (`REV-E-16`, `REV-E-17`) were caught **after publication, by a peer process**, and
both were counting defects in the artefacts that exist to make counting possible. No error
in this round was caught by the author re-reading its own published text.

**The `REV-E-16` / `REV-E-17` pair is the sharpest single lesson of the session.** Both were
found because P04 re-executed a table it had already published twice, in a package about
counting discipline, and then told P07 to do the same. Neither would have been found by any
control this session ran, because every one of those controls checked *claims* and neither
error was in a claim — they were in totals. A control that validates findings does not
validate the arithmetic that describes them.

## 5. Method Notes for the Next Round

| # | Note |
|---|---|
| `REV-M-01` | Every negative claim in this package was produced by a pattern that is recorded in `13 §4` **with its false-negative modes**. Two of the four patterns are name-based and would miss a Thai tax rule implemented with no Thai, tax or withholding token in its identifiers (`U-11`). |
| `REV-M-02` | No database and no runtime evidence was used (`U-02`). Every behavioural statement is derived from source. Statements about what a user would observe (`04 §5`) are derivations, not observations, and are labelled as such. |
| `REV-M-03` | The declared source set is the Account module's own source index. Which addon copy is deployed in production is `U-01` and was not determined. Findings bind to the declared set. |
| `REV-M-04` | Under `EC-07`, two consecutive clean independent passes are required before a Final Research Gate. This session is **one** pass with one round of independent challenge. It cannot and does not claim `EC-07`. |
| `REV-M-05` | `U-12` (excess-VAT carry-forward mechanism) was opened as an untraced unknown and **closed within the session** by reading the report expression tree. Closing it produced `P07-F-40`, which is more material than the unknown was. Two further inferences were tested during that trace and refuted: that the carry-forward was unimplemented, and that the return periodicity was simply unset rather than defaulted. Both are recorded here rather than published as findings. |
| `REV-M-06` | `P07-U-14` was opened as `HOLD — SCOPE EVIDENCE REQUIRED` and **closed as a decidable finding** during the round: the tenant boundary is specified in this very clone at status `NEW`, and no tenant ORM model exists anywhere on the volume. The routing that would have deferred it to P11 said the evidence lay "outside the P07 population" — it lay six directories up, in the same working tree. This is the programme's recorded "never declare no-access from a working-tree search" defect recurring in a milder form, and it was caught by a reviewer, not the author. |
| `REV-M-07` | The controls that worked in this round were, in order of yield: **running a declared pattern** (8 self-caught errors), and **disjoint adversarial review with an explicit instruction to report wrong paths in the brief** (15 corrections, 31 new findings, 2 severity escalations). The control that yielded nothing was re-reading the draft. A next round should spend its self-review budget on executing declared patterns rather than on re-reading. |
