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

## 5. Method Notes for the Next Round

| # | Note |
|---|---|
| `REV-M-01` | Every negative claim in this package was produced by a pattern that is recorded in `13 §4` **with its false-negative modes**. Two of the four patterns are name-based and would miss a Thai tax rule implemented with no Thai, tax or withholding token in its identifiers (`U-11`). |
| `REV-M-02` | No database and no runtime evidence was used (`U-02`). Every behavioural statement is derived from source. Statements about what a user would observe (`04 §5`) are derivations, not observations, and are labelled as such. |
| `REV-M-03` | The declared source set is the Account module's own source index. Which addon copy is deployed in production is `U-01` and was not determined. Findings bind to the declared set. |
| `REV-M-04` | Under `EC-07`, two consecutive clean independent passes are required before a Final Research Gate. This session is **one** pass with one round of independent challenge. It cannot and does not claim `EC-07`. |
