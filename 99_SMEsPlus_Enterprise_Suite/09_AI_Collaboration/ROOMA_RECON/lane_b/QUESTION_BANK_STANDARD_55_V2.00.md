# ROOM A — THE STANDARD 55
## Applies to EVERY module in scope, without exception

**Version:** V2.00 — supersedes `QUESTION_BANK_STANDARD_35_V1.00`
**Date:** 2026-09-22 · Asia/Bangkok
**Status:** `PREPARED ONLY / READY FOR FREEZE`
**Boss decision:** Option **B**, 2026-09-22 — merge both global sets rather than discard either
**Authors:** Q01–Q35 RED TEAM draft, corrected on Boss instruction · Q36–Q55 **GMVQ / OVQDT**
(Odoo Functional + Tester/QA + SaaS Architecture Consultant), from `GMVQ-G01-STD35-V1.00`

---

## 1. Why this set grew from 35 to 55

Two global question sets existed, written independently, on **different axes**:

| Set | Axis | What it asks |
|---|---|---|
| RED TEAM 35 | Business / ERP | what does it do · when does it post · when do goods move · tax · numbering |
| GMVQ 35 | Platform / safety | does it leak across customers · what happens when it breaks · is the audit trail trustworthy |

Measured overlap: **15 GMVQ questions were already covered** by the business set and are absorbed
(§4 records where each one went). **20 were not covered by anything** — and the business set had
**zero** questions on isolation, concurrency, or failure behaviour.

Conversely GMVQ had **zero** accounting, **zero** tax, **one** inventory and **zero**
approval-separation questions — the four areas Boss mandated for the common floor.

Discarding either set would have removed something the Constitution requires. So neither was
discarded.

```
STANDARD           55   = 35 business/ERP  +  20 platform integrity
Module-specific   ≥40   unchanged
Combined floor    ≥95   per module        (was ≥75)
```

**The floor is Minimum Research Depth.** It is not a completion percentage and not a Formal
Coverage denominator (REV-A P5 qualifier). Formal Coverage remains **NOT AUTHORIZED** until a
Canonical Function-ID denominator is Boss-frozen.

Workload at the new floor: **247 × 95 = 23,465 answers per lane.** Questions to author is
unchanged at 9,880 — the 20 new standard questions are written once and used by all 247 modules.

---

## 2. Rules every answer operates under

| # | Rule |
|---|---|
| 1 | All **55** are touched for every module. No exceptions, no tiering. |
| 2 | Valid answers: `ANSWERED` (with artifact) · `NOT_APPLICABLE` (with reason) · `NOT_OBSERVED` / `NOT_FOUND_IN_SOURCE` (with what was tried) |
| 3 | Every question carries a `DISCONFIRMING_OBSERVATION`. CI rejects one without it. |
| 4 | Question text contains no model, field, method, module name, XML ID or vendor identifier — it would leak the answer to the blind lane. |
| 5 | Every answer carries `LAYER: BASE` or `LAYER: PROCESS`. |
| 6 | Join key is `MODULE + QID` — a Research Evidence Join Key only, never a Canonical Function-ID. |
| 7 | Rolling Batch Freeze: freeze per module or per batch before either lane starts that batch. |
| 8 | Padding is forbidden. A question that cannot fail is not a question. |

---

## 3. THE STANDARD 55

### A. Behaviour and lifecycle — Q01–Q10
*Constitution §12: the list an agent must never guess.*

**STD-Q01 — Business purpose** · What business outcome does this capability exist to produce, stated without naming the system?
`DISCONFIRM:` the capability produces no outcome a business user would ask for.

**STD-Q02 — Who may use it** · Which roles can reach this capability, and which are blocked?
`DISCONFIRM:` a role with no business reason can reach it.

**STD-Q03 — Entry points** · By what routes can this be started — screen, scheduled job, automation, external call?
`DISCONFIRM:` a route exists that no one documented, e.g. it can be triggered without a user.

**STD-Q04 — Records created or changed** · What business records come into existence or change as a result?
`DISCONFIRM:` a record changes that the user was never told about.

**STD-Q05 — Mandatory data** · What must be supplied before the system will let the work proceed?
`DISCONFIRM:` the work proceeds with a mandatory value missing.

**STD-Q06 — States** · What states can the business document occupy, from creation to final?
`DISCONFIRM:` a state exists that is reachable but not listed.

**STD-Q07 — Transition triggers** · What causes each state change — a person, a rule, a schedule, another document?
`DISCONFIRM:` a state changes with no identifiable trigger.

**STD-Q08 — Blocking validations** · Which rules stop the work, and what does the user see when they do?
`DISCONFIRM:` a rule that should block, warns only, and the work completes.

**STD-Q09 — Negative path** · What happens when the work fails midway — is it fully undone, or partly applied?
`DISCONFIRM:` a failure leaves the records in a half-changed state.

**STD-Q10 — Repetition and duplication** · What happens if the same action is performed twice, or by two people at once?
`DISCONFIRM:` duplicate business documents are created with no warning.

---

### B. Approval, execution and posting separation — Q11–Q14
*Constitution §3.2. Mandatory for SMEsPlus, so every module is tested for it.*

**STD-Q11 — Approval requirement** · Does anything here require approval before it may proceed, and who approves?
`DISCONFIRM:` something with financial effect proceeds with no approval at all.

**STD-Q12 — Approval does not execute** · When approval is given, does the business transaction execute immediately as part of that act?
`DISCONFIRM:` approving also executes the transaction in the same step.
*The single most important structural question in the set.*

**STD-Q13 — Who executes** · What actually performs the business transaction, and is it separable from the approval?
`DISCONFIRM:` execution cannot be separated from approval.

**STD-Q14 — Posting trigger** · What exact event causes accounting posting — approval, confirmation, delivery, payment, a date?
`DISCONFIRM:` posting happens inside the approval step, or at a point nobody can name.

---

### C. Accounting — Q15–Q22
*Constitution §13.*

**STD-Q15 — Journal entries produced** · What accounting entries result, and when?
`DISCONFIRM:` an entry appears that the business event does not justify.

**STD-Q16 — Debit and credit logic** · Which side moves, against what, and on what basis is the account chosen?
`DISCONFIRM:` the account chosen changes with no rule the business can state.

**STD-Q17 — Posting date versus document date** · Which date drives the accounting, and can they differ?
`DISCONFIRM:` posting lands in a period the user did not intend and was not warned about.

**STD-Q18 — Accounting period control** · Can a back-dated entry land in a closed period, and who may override?
`DISCONFIRM:` a closed period accepts a new entry.
*Statutory exposure — a filed financial statement changing after filing.*

**STD-Q19 — Reversal** · How is a posted entry reversed, and what does the reversal look like in the ledger?
`DISCONFIRM:` a posted entry can be deleted rather than reversed.

**STD-Q20 — Cancellation and correction** · Can a confirmed business document be cancelled or corrected, and what happens to what it produced?
`DISCONFIRM:` cancellation leaves the accounting effect in place.

**STD-Q21 — Reconciliation impact** · What does this leave open to be matched later, and how is the match recorded?
`DISCONFIRM:` an item is marked matched without a counterpart.

**STD-Q22 — Financial report impact** · Which financial reports change as a result, and by how much?
`DISCONFIRM:` a report changes in a way the underlying entries do not explain.

---

### D. Tax, money and numbering — Q23–Q26
*Constitution §13. Thai statutory relevance.*

**STD-Q23 — Tax basis and VAT** · On what amount is tax computed, and what determines the rate?
`DISCONFIRM:` the base or rate changes with no rule an accountant can state.
`LEGAL_TAX_REVIEW_REQUIRED` if Thai treatment cannot be established from evidence.

**STD-Q24 — Withholding tax** · Is withholding applied, at what point in the flow, on what base, and what document is produced?
`DISCONFIRM:` withholding is computed on a base that differs from the payment it accompanies.
`LEGAL_TAX_REVIEW_REQUIRED` if the Thai rule cannot be established from evidence.

**STD-Q25 — Currency, exchange and rounding** · How are foreign amounts converted, at what rate and date, and where does rounding land?
`DISCONFIRM:` a rounding difference disappears instead of being posted somewhere.

**STD-Q26 — Document numbering** · How is the document number produced, is it gapless, can it be reused or altered, and does it stay unique when several are created at the same instant and across separate company or customer boundaries?
`DISCONFIRM:` a number can be changed after posting, reused, duplicated under simultaneous creation, or drawn from another boundary's series.
*Strengthened in V2.00 by absorbing GMVQ-24.*

---

### E. Multi-tenant, security and audit — Q27–Q30
*Constitution §3.3. Every uncertainty here is a Blocker by constitutional rule, not a note.*

**STD-Q27 — Company, branch and tenant scope** · Which company, branch and tenant does the data belong to, and what enforces that boundary?
`DISCONFIRM:` a record exists that belongs to no scope, or to more than one.

**STD-Q28 — Cross-boundary visibility** · Can a user of one company, branch or tenant see, reach or affect another's data — by screen, report, search, export, download, print, bulk read or external call?
`DISCONFIRM:` any route returns another boundary's data.
*A single positive here is a critical finding, not a note. Strengthened in V2.00 by absorbing GMVQ-01 and GMVQ-05.*

**STD-Q29 — Permission and record-level access** · Beyond menu visibility, what limits which individual records a user may read, change or delete?
`DISCONFIRM:` menu access alone determines record access.

**STD-Q30 — Audit trail and configuration ownership** · What is recorded about who changed what and when, who can change the configuration behind this capability, and can the trail itself be altered?
`DISCONFIRM:` a change of financial or permission consequence leaves no trace, or the trace can be edited.
*Strengthened in V2.00 by absorbing GMVQ-27.*

---

### F. Goods movement and the inventory–accounting bridge — Q31–Q35
*Added on Boss correction, 2026-09-22: in practice almost every module touches Inventory and Account, so both belong in the common floor.*

**STD-Q31 — Physical quantity effect** · Does this capability create, consume, reserve or move physical quantity, and between which places?
`DISCONFIRM:` quantity on hand changes without a goods movement anyone can point to.

**STD-Q32 — What actually moves the goods** · Which event moves the goods, and is it the same event that confirms the business document?
`DISCONFIRM:` goods move before the document has reached a state that authorises the movement.

**STD-Q33 — Inventory-to-accounting bridge** · Does the goods movement produce an accounting entry, at what moment, and at what value?
`DISCONFIRM:` goods move with no valuation entry, or the entry carries a value the business cannot explain.
*The join between Q14 and Q31. Most large ERP errors live exactly here: goods moved in one period, cost recognised in another.*

**STD-Q34 — Shortage and negative quantity** · What happens when there is not enough stock — blocked, warned, or allowed to go negative?
`DISCONFIRM:` quantity on hand goes below zero with no control and no record of who allowed it.

**STD-Q35 — Unit of measure** · Can the quantity be expressed in more than one unit, how is conversion performed, and where does the rounding land?
`DISCONFIRM:` converting to another unit and back does not return the original quantity.

---

### G. Platform integrity and multi-tenant safety — Q36–Q55
*New in V2.00. Authored by GMVQ / OVQDT. These ask what happens when the system is under
stress, interrupted, automated, or crossed — the failures that pass every happy-path test.*

**STD-Q36 — Indirect relationship traversal** · Following related records, references, smart navigation, history or activity links — does the boundary hold on every hop?
`DISCONFIRM:` a permitted record contains a relationship path that opens or reveals data from another boundary.

**STD-Q37 — Search, suggestion and picker leakage** · Do search, autocomplete, recent items, suggestions and reference pickers reveal only what the active context permits?
`DISCONFIRM:` a restricted record appears in search results, suggestions, recent items or a picker — even if opening it is blocked.

**STD-Q38 — Aggregate and count leakage** · Are counts, totals, grouped summaries, dashboards and graphs computed only from data the active context can see?
`DISCONFIRM:` a total, count, group or chart changes because of records the user cannot otherwise see.
*A system can hide every row and still leak the confidential total.*

**STD-Q39 — Attached and derived content boundary** · Do attachments, generated documents, previews, thumbnails, extracted text and search indexes carry the same boundary as the parent record, through upload, preview, search, download and deletion?
`DISCONFIRM:` a user who cannot reach the parent record can still retrieve its file, preview, thumbnail or indexed text.

**STD-Q40 — Parallel context confusion** · When one user is authorised in more than one company or customer context, do parallel sessions or tabs each stay bound to their own explicit context?
`DISCONFIRM:` acting in one context causes a read or write under the other, with no permission bypass visible anywhere.

**STD-Q41 — Context switch with work in progress** · Can changing company or customer context while a record is already open cause that work to be saved, confirmed or posted under the unintended one?
`DISCONFIRM:` a record opened under one company is committed under another, or silently acquires the other's defaults.

**STD-Q42 — Authorisation change takes effect, both directions** · When permission is granted or revoked, does the change take effect consistently and promptly across every supported path, including any cached decision?
`DISCONFIRM:` a revoked user keeps acting through a stale decision, or a granted user is allowed by one path and denied by an equivalent one.

**STD-Q43 — Interrupted operation, knowable outcome** · When a session expires or a request times out during a state-changing action, is the result either fully applied or not applied — and can the user reliably discover which before retrying?
`DISCONFIRM:` some effects are durable and others missing with no recoverable status, or the user has no trustworthy way to tell and a retry creates a second effect.

**STD-Q44 — Concurrent and conflicting changes** · When two authorised actors change the same object at nearly the same time — including incompatible actions such as confirm against cancel — is the outcome deterministic, is one coherent final state preserved, and can the trail say which prevailed?
`DISCONFIRM:` a later save silently discards an earlier one, both incompatible actions appear to succeed, or the final state mixes both with no rule.

**STD-Q45 — Unattended execution stays in scope and stays deterministic** · Does automated or scheduled work run under an explicit, auditable company and customer scope, and does one logical run behave consistently even if configuration changes while it is running?
`DISCONFIRM:` an automated task touches records outside its intended scope, or records in one run follow different rules solely because configuration changed mid-run, with no version trace.

**STD-Q46 — Default-value contamination** · Are suggested and inherited defaults derived only from the active context, unless a sharing rule is explicit and authorised?
`DISCONFIRM:` a new record in one context automatically receives a value owned exclusively by another.
*This is how another company's account, warehouse, sequence or owner gets written into new data without anyone bypassing a permission.*

**STD-Q47 — Copy and duplicate recalculate what matters** · Does copying a record recompute ownership, scope, permission-sensitive defaults and lifecycle state, rather than carrying values that are unsafe in the new context?
`DISCONFIRM:` the duplicate inherits restricted ownership, scope, approval state or permission-derived values that a newly created equivalent would not receive.

**STD-Q48 — Archive and delete leave no usable orphan** · When a parent is archived, disabled or removed, do dependent references, shortcuts, attachments and historical links stop being a way in?
`DISCONFIRM:` a dependent or historical link still permits an action or a view that the parent's new state should prohibit.

**STD-Q49 — Shared data has explicit ownership rules** · For data visible in more than one company or customer context, is there an explicit rule separating visibility from ownership, edit authority and financial scope?
`DISCONFIRM:` a user alters shared-looking data in a way that changes another company's operational or financial behaviour, with no stated shared-governance rule.

**STD-Q50 — Time zone and date boundary** · Does the same business event have one authoritative business date for every user, wherever they are?
`DISCONFIRM:` the same event falls into different business dates or periods solely because the acting user's time zone differs.

**STD-Q51 — Notification and recipient isolation** · Are notifications, messages, reminders and recipient lists recalculated from current authorisation and ownership at the moment of delivery?
`DISCONFIRM:` someone who no longer has access receives restricted content, a restricted identifier, or a link that reveals it.

**STD-Q52 — Automated action keeps an accountable identity** · Can an automated change be told apart from a human one, and traced back to the rule or event that caused it?
`DISCONFIRM:` an automated change is indistinguishable from an unexplained generic user action, or cannot be linked to what initiated it.

**STD-Q53 — Out-of-band data operations preserve the boundary** · Do restore, rollback, repair, upgrade and migration operations keep records, permissions and files in the company and customer context they belonged to?
`DISCONFIRM:` a restored, repaired or migrated object becomes visible, owned, editable or differently scoped in a context it did not belong to, with no explicit migration rule and evidence.
*Recovery and upgrade tooling routinely bypasses the application's own controls.*

**STD-Q54 — Every path enforces the same controls** · Is the same business effect subject to equivalent authorisation, validation, scope and audit whether it is done on screen, in bulk, by import, by automation or through any other supported channel — including per-record checks and a deterministic result when only part of a selection is valid?
`DISCONFIRM:` an action blocked or validated in one path succeeds through another without equivalent control, or a bulk run touches a restricted record, skips failures with no trace, or leaves an unexplained partial state.

**STD-Q55 — One customer cannot destabilise another** · Can heavy, malformed or repeatedly failing work in one customer context consume shared capacity or block processing such that an unrelated customer loses availability or correctness?
`DISCONFIRM:` sustained load or a failure loop in one context causes an unrelated context to fail, corrupt data, or stay blocked indefinitely, with no protective control.

---

## 4. Provenance — where every GMVQ question went

**Absorbed into an existing question (15).** Nothing was dropped; each strengthened its host.

| GMVQ | Subject | Absorbed into |
|---|---|---|
| GVQ-01 | Cross-customer direct isolation | STD-Q28 |
| GVQ-05 | Export and bulk-read isolation | STD-Q28 (route list) · STD-Q54 |
| GVQ-09 | Revocation during in-flight action | STD-Q42 |
| GVQ-10 | Grant propagation consistency | STD-Q42 |
| GVQ-11 | Session expiry mid-operation | STD-Q43 |
| GVQ-12 | Concurrent / lost update | STD-Q44 |
| GVQ-13 | Duplicate-submit idempotency | STD-Q10 · STD-Q43 |
| GVQ-14 | Partial-failure atomicity | STD-Q09 · STD-Q43 |
| GVQ-15 | Ambiguous timeout recovery | STD-Q43 |
| GVQ-17 | Config change mid-run | STD-Q45 |
| GVQ-18 | Stale authorisation cache | STD-Q42 |
| GVQ-24 | Unique numbering under concurrency | STD-Q26 |
| GVQ-25 | Upload metadata boundary | STD-Q39 |
| GVQ-27 | Audit completeness and immutability | STD-Q30 |
| GVQ-30 | Bulk scope and partial error | STD-Q54 |

**Promoted to a new standard question (20).**

| GMVQ | → | GMVQ | → | GMVQ | → |
|---|---|---|---|---|---|
| GVQ-02 | Q36 | GVQ-19 | Q46 | GVQ-31 | Q55 |
| GVQ-03 | Q37 | GVQ-20 | Q47 | GVQ-32 | Q55 |
| GVQ-04 | Q38 | GVQ-21 | Q48 | GVQ-33 | Q53 |
| GVQ-06 | Q39 | GVQ-22 | Q49 | GVQ-34 | Q54 |
| GVQ-07 | Q40 | GVQ-23 | Q50 | GVQ-35 | Q44 |
| GVQ-08 | Q41 | GVQ-26 | Q51 | | |
| GVQ-16 | Q45 | GVQ-28 | Q52 | | |
| GVQ-29 | Q53 | | | | |

**Seven pairs were merged** because they test the same failure from two angles, and two questions
answered by the same evidence are padding: 09+10+18 → Q42 · 11+15 → Q43 · 12+35 → Q44 ·
16+17 → Q45 · 29+33 → Q53 · 30+34 → Q54 · 31+32 → Q55.

Every GMVQ `DISCONFIRMING_OBSERVATION` survives, either as its own question's disconfirm or folded
into the host's. **No GMVQ failure mode was lost.**

---

## 5. What this set still does not cover — deliberately

| Not covered | Where it belongs |
|---|---|
| Anything module-specific | the ≥40 module-specific questions |
| Performance thresholds and SLAs | Infrastructure Gate, not ROOM A |
| Code quality, style, structure | out of scope — this is a behavioural study |
| Formal Coverage percentages | **NOT AUTHORIZED** until a Canonical Function-ID denominator is Boss-frozen |

---

## 6. Gaps, risks and blockers

| ID | Item | Severity |
|---|---|---|
| `RT-Q55-001` | Q36–Q55 were authored for a platform group. For a small leaf module several will legitimately be `NOT_APPLICABLE` — that is a valid answer and **must not** be treated as a coverage failure. Watch for teams inflating `NOT_APPLICABLE` to avoid work; the reason field is the control. | MEDIUM |
| `RT-Q55-002` | Q55 (noisy neighbour) and parts of Q45 need a controlled load or a deliberately failing workload. On the shared study instance that risks disturbing the other lane. **Schedule these, do not run them ad hoc.** | MEDIUM |
| `RT-Q55-003` | The floor moves 75 → 95, so every prior workload figure is superseded. Baseline change-log entry required. | ADMIN |
| `RT-V2-003` | RED TEAM drafted Q01–Q35 and this merge, and cannot certify either. Q36–Q55 are GMVQ's work, reviewed by RED TEAM. | PROCESS |

---

## 7. Required next action

| # | Action | Owner |
|---|---|---|
| 1 | Review the merge — especially the seven pairs in §4 | GMVQ / OVQDT |
| 2 | Freeze the Standard 55 | Boss |
| 3 | Author ≥40 module-specific per module for Wave 1's 23 modules | GMVQ + Functional |
| 4 | Update the Baseline change log: floor 75 → 95, answers per lane 18,525 → 23,465 | PMO |

---

```text
This output is a review and merge result only. It is not Boss Final Approval.
Executed on Boss decision "B", 2026-09-22 — merge rather than discard.
Q01–Q35 are RED TEAM's draft as corrected by Boss; Q36–Q55 are GMVQ/OVQDT's work, merged and
edited for consistency by RED TEAM, which therefore cannot certify the result.
No Formal Coverage figure is claimed or authorized.
```
