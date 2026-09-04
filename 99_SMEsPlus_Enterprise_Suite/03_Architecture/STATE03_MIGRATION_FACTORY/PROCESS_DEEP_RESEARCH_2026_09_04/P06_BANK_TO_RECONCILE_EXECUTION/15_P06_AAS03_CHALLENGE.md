# P06_AAS03_CHALLENGE.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE

**Standing:** four AAS-03 experts challenge every level. Dissent is preserved, not resolved. Where an expert and the package disagree and the evidence does not settle it, **both positions stand** and the matter is recorded as open.

**Reading instruction (adversarial-section discipline):** cite this file's challenges and the package's responses. **Do not cite the headline tables of the evidence files** — the corrections live here and in §8 of each register, not in the summaries.

---

## Expert 1 — Accounting Integrity

**AAS1-C-01 — "You claim four states are not independent. Prove the negative isn't just your reading."**
Response: it is not a reading. `account.payment.state` declares `@api.depends('invoice_ids.payment_state', 'move_id.line_ids.amount_residual')` at `$V18E/account/models/account_payment.py:411` and `account.move._compute_payment_state` reads `matched_payment_ids.state`. Two stored computed fields each depending on the other is a structural fact, not an interpretation. **Challenge answered.**

**AAS1-C-02 — "PSM-F-13 says an invoice can be settled with a non-zero residual. That would be a catastrophic, widely-reported bug. Are you sure?"**
Response: the branch is explicit at `$V18E/account/models/account_move.py:1213-1218` and is conditioned on `not p.move_id` — a payment with **no journal entry**. It is reachable only when no outstanding account is configured (PSM-F-07). So the correct statement is narrower than "an invoice can be settled with a residual": it is **"in a configuration where payments generate no accounting, the invoice status is driven by the payment record alone."**
**Package amended:** PSM-F-13's severity is retained but the precondition is now stated in the finding. **Partially conceded.**

**AAS1-C-03 — "You call cell 9 the only coherent terminal cell. You characterised 18 of 60 cells. That is a claim about 42 cells you did not examine."**
Response: conceded, and the file already says so — the remaining 42 are marked Class C. But the sentence *"there is exactly one fully coherent terminal cell"* over-reaches beyond the 18 examined.
**Package amended:** restate as *"of the 18 cells characterised, exactly one is fully coherent."* **Conceded.**

**AAS1-C-04 — "EGL-F-10 accuses a custom module of expensing an asset. That is a serious accusation resting on a default value."**
Response: agreed, and the finding already carries the qualification and a HOLD. The default resolves to the product's expense account; **which account the configured product actually carries is not in the searched scope.** No accusation is made — a question is raised and routed. **Challenge answered; the qualification stands as written.**

## Expert 2 — Controls and Audit

**AAS2-C-01 — "Seven CONFIRMED DEFECT classifications is a lot. Is the bar right?"**
Response: the bar is *provable from quoted source with no interpretation*. Each of the seven meets it: A1 (four doors with no identity, plus three fail-open enforcement points), A3 (advisory-only, plus a state value absent from the selection), A4b (three guards each admitting `False`), A4c (two record rules, one wider than the other), A5 (two destructive paths, zero statement-line awareness), A6 (a five-file zero-hit denominator), A7 (an eight-line quote containing its own bypass). **Challenge answered.**

**AAS2-C-02 — "A6 is your strongest claim and it rests on zero-hit greps. Zero hits prove your pattern found nothing, not that nothing exists."**
Response: correct in general, and this is the standing project lesson. Here the negative is corroborated **positively**: the two hits that do exist in `account_partial_reconcile.py` are at `:513-514` and are shown to be a *date relocation*, not a gate. A positive demonstration that the only lock-date code on the path relocates rather than refuses is stronger than the absence elsewhere. **Challenge answered — and the corroboration is the reason it survives.**

**AAS2-C-03 — "RM-F-30 says a lock control exists by accident. You then rely on it in the narrative."**
Response: the file marks it medium-high confidence, states it was read and not executed, and carries `P06-OQ-20` saying it must be tested before reliance. **No requirement in this package depends on it.** **Challenge answered.**

**AAS2-C-04 — "You found no approval control on write-offs. Did you search the right layer? Approvals in this estate live in `multi_level_approval`, which you did not search."**
Response: **conceded, and material.** Three search scopes were declared, all inside `$V18E`. `$CUST18` contains `multi_level_approval`, `multi_level_approval_configuration` and `multi_level_approval_hr`, **none of which was searched for write-off or reconciliation coverage.**
**Package amended:** EC-F-08 and `P06-B-22` are **re-classified from Class A to Class B** — not found in the searched scope, where the searched scope excludes the custom approval modules. New open item `P06-OQ-81`.
**This is the single most valuable challenge in this file, and it is a downgrade of one of the package's own findings.**

## Expert 3 — Multi-Company and Scope

**AAS3-C-01 — "Your A4 downgrade under CORR1 is convenient. Are you softening a finding to fit a new rule?"**
Response: a fair challenge and it deserves a direct answer. The downgrade is confined to **one vector** (sibling branches) and is explicitly conditional on a question the package cannot answer from source. **A4b and A4c were retained and strengthened, and C-11 was newly raised by the same correction.** A correction that produced three downgrades and one new HIGH contradiction is not being used selectively. **Challenge answered.**

**AAS3-C-02 — "SCOPE-F-04 says you cannot tell whether `root_id` means one legal entity. Could you not have determined it from the runtime extract?"**
Response: **conceded as a gap.** The runtime extract (S-04) shows two companies, C1 and C2, with **disjoint bank journals and different legacy chart-of-account codes** — evidence they are distinct accounting entities. It does **not** show their `parent_id` / `root_id` relationship, which is the actual question.
**Package amended:** SCOPE-F-04 now records that the available runtime evidence is *suggestive of distinct entities but silent on the hierarchy*, and that resolving it needs one query the session could not run. The HOLD stands, better argued. **Partially conceded.**

**AAS3-C-03 — "CPO-F-04 claims 12 bank journals map to 2 GL accounts. That is one CSV. Is it a census?"**
Response: no, and the file says so. The finding is bounded to that extract's 12 rows and explicitly refuses the form "the system has N bank journals." **Challenge answered.**

**AAS3-C-04 — "You assign currency rate to TENANT. On what authority?"**
Response: business semantics — a rate table is shared reference the customer maintains, it is not a legal-entity fact, and unrelated customers must not share one (CORR1: unrelated independent companies are separate tenants by default). The reference implementation disagrees by holding rates globally, and **that disagreement is recorded as the finding**, not resolved in the package's favour. **Challenge answered, with the disagreement preserved.**

## Expert 4 — Migration and Deployment Reality

**AAS4-C-01 — "Your entire custom-module analysis rests on copies you cannot attribute. What is it worth?"**
Response: it is worth exactly what it claims — the copies are byte-identical at the Python layer (CMD-F-01), so behavioural findings hold for whichever is deployed. What cannot be claimed is *set membership*, and the package makes no deployment assertion anywhere. **Challenge answered.**

**AAS4-C-02 — "You call the missing PDC support 'the largest single functional regression'. Compared to what baseline? Perhaps PDC was never used."**
Response: **conceded.** The claim compares module presence in v14 against absence in v18. It does **not** establish that the v14 modules were installed, used, or carry data.
**Package amended:** restated as *"the largest functional capability present in the v14 custom set and absent from all three v18 custom sets."* Whether it was used is `P06-OQ-82` — answerable only from the v14 database.
**A second, sharper point stands regardless:** post-dated cheques are ordinary Thai commercial practice, so the capability question is live whether or not the v14 modules were used.

**AAS4-C-03 — "EC-F-15 says an enterprise wizard has no Python producer. The likelier explanation is an incomplete copy, and you present it as a finding."**
Response: the file presents **both readings and refuses to choose** (T-01), and prescribes the diff that would settle it. It is recorded as an open question, not a defect. **Challenge answered.**

**AAS4-C-04 — "PPT-F-08 claims accounting is created outside the webhook transaction. That is an architectural claim from three call sites."**
Response: the denominator is declared — all `_post_process` call sites in `$V18E/payment`, non-test, of which three exist and none is a notification path. The cron's `active=False` default and the browser-session-keyed poll are both quoted. **Challenge answered.**

---

## Cross-cutting challenge — all four experts

**AAS-X-01 — "You produced twenty files from eight parallel streams. How much did you verify yourself?"**
Response, given honestly: the session read the core state-model evidence **before** delegating, so the canonical-question answer rests on first-hand reading. The remaining findings rest on the streams' quoted evidence. **Two independent checks were run and both found errors** — the denominator misstatement (REV-E-01) and the source-tree ambiguity (REV-E-04, contradiction T-03). **Neither of those was found by the stream that produced it.**
**This is consistent with the programme's standing lesson that independent review is the only control that has caught this class of defect**, and it is a reason to weight this package's positives above its negatives at the gate.

**AAS-X-02 — "Which of your findings would you retract first if one had to go?"**
Response, in order: (1) `P06-B-22`, the write-off approval finding, already downgraded to Class B by AAS2-C-04; (2) A7 problem 2, the orphaned move, which is inferred rather than quoted; (3) `P06-B-21`, the vendor-advance expense finding, which is entirely data-dependent and already HOLD.
**The three the package would defend hardest:** A6 (lock dates do not gate reconciliation) — a five-file denominator with positive corroboration; C-01 (`is_matched` is true without a bank statement) — two quotes, no interpretation; PPT-F-10 (the provider reference is unconstrained and never read) — a tree-wide zero plus a three-occurrence census.

---

## Amendments this challenge produced

| # | Amendment | Type |
|---|---|---|
| 1 | PSM-F-13 precondition stated in the finding | narrowing |
| 2 | Settlement-matrix coherence claim bounded to the 18 characterised cells | narrowing |
| 3 | **EC-F-08 / `P06-B-22` re-classified Class A → Class B**; custom approval modules unsearched | **downgrade** |
| 4 | SCOPE-F-04 now records what the runtime extract does and does not show | strengthening of argument |
| 5 | PDC regression claim restated against a declared baseline | narrowing |
| 6 | New open items `P06-OQ-81` (approval modules), `P06-OQ-82` (v14 PDC usage) | new |

**Six amendments, of which one is a classification downgrade of the package's own finding.** A challenge round that produces no downgrades has not been run.

---

## Dissent preserved

| ID | Position | Counter-position | Status |
|---|---|---|---|
| DIS-01 | Currency rate is TENANT-scoped | The reference holds rates globally, implying PLATFORM | **Both stand.** The package asserts the semantics; the implementation disagrees; the disagreement is the finding. |
| DIS-02 | The batch-rejection wizard is unreachable in this build | The evidence copy is an incomplete checkout | **Both stand.** T-01. |
| DIS-03 | Sibling-branch reconciliation crosses a company boundary | `root_id` may legitimately be the company boundary | **Both stand.** SCOPE-F-04, `P06-B-27`. |
| DIS-04 | The custom vendor advance expenses an asset | The configured product may carry a prepayment account | **Both stand.** Data-dependent, HOLD. |

---

# End
