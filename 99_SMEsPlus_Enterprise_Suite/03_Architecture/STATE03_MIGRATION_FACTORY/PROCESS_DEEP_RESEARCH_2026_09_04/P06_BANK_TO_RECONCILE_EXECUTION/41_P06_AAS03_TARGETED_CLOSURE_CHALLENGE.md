# P06_AAS03_TARGETED_CLOSURE_CHALLENGE.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C12)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Scope:** a **fresh** challenge on the closures and modifications made by this continuation. The prior round's 18 challenges stand and are not re-run.

Each expert must identify: **false-positive closure risk · absence-from-incomplete-population risk · cross-process ownership risk · financial integrity risk.** Consensus is not forced.

---

## Expert 1 — Leader Functional Design

**E1-C-01 — On `B-27`: you closed the programme's flagship blocker without touching a database. Is that a false-positive closure?**
**Response — challenge answered.** The blocker asked what `root_id` *denotes*. That is a model question, and the model answers it: five delegated fields, `vat` and `company_registry` not among them, no constraint forcing branch VAT equality. **A database could only have told us what one deployment currently contains — it could not have told us what the model permits tomorrow.** The closure is on the stronger evidence, not the weaker.
**Corroboration the response does not rely on but should be recorded:** P02 `SF-06` reached the same conclusion independently, before P06 closed it.

**E1-C-02 — You reversed a downgrade you made one round earlier. Which round was wrong?**
**Response — neither, and this is worth stating precisely.** The prior downgrade to HOLD was correct **on the evidence then available**: the question was genuinely open and guessing would have been worse. This round's upgrade is correct **on new evidence**. **A finding that moves in both directions across rounds is behaving properly if each move is evidenced.** What would be improper is a finding that only ever moves in the direction that flatters the author — and this package now has 5 upgrades, 2 downgrades and 1 reclassification.

**E1-C-03 — `25_` specifies a target state model. Is that not designing, which the prompt forbids?**
**Response — partially conceded, and the boundary is thin.** `25_` §4 states four facts, their owners, and five invariants. That is closer to specification than to research. **The defence:** the prompt requires *"determine the actual semantic state model"*, and a semantic model that omits what the states must mean is not a model. **The concession:** §4's transition table is a design proposal and is labelled as such nowhere in the file. **Amendment applied:** `25_` §4 is to be read as `DESIGN CANDIDATE`, not `FACT VERIFIED`. Recorded.

**E1-C-04 — `P06-B-53`, the eighth door — is that P06's finding or P05's?**
**Response — it is P05's finding and P06's problem.** It is cited to P05 `SR-04` throughout. **The risk the challenge is really pointing at is cross-process ownership:** P06 has absorbed a peer finding into its own blocker register, which could double-count at P11. **Amendment:** `P06-B-53` is marked as *inherited from P05 `SR-04`* so P11 can deduplicate. Recorded.

---

## Expert 2 — Leadership Database Design

**E2-C-01 — Every deployment question in this package is unresolved, and you closed `OQ-71`, `OQ-81` and `OQ-21` anyway. On what basis?**
**Response — challenge answered, with the distinction made explicit.** Those three are **source** questions, not deployment questions. *"Does `om_data_remove` contain an unguarded `DELETE FROM`"* is answerable by reading it. *"Is `om_data_remove` installed"* is not, and is **not** claimed. `24_` classifies every module as `UNKNOWN` for the target precisely because the registry is absent.

**E2-C-02 — You found the evidence tree is a filtered distribution (`P06-B-55`). Does that not invalidate every tree-scope negative?**
**Response — conceded in part, and it is the sharpest challenge in this file.** It does not *invalidate* them — each was declared with its path set, and this build is the correct target. But it **changes what "tree scope" means**, and the package used that phrase as though it meant "Odoo 18".
**Amendment applied:** every tree-wide Class-A negative now inherits the filtered-build boundary explicitly. `P06-B-55` is the carrier.
**And a residual risk the response cannot dismiss:** if the distribution was filtered by module *selection*, a capability could have been filtered out that a full Odoo 18 ships. **For the fee and returned-item negatives this is now low risk** — the Thai packs are present and carry neither — but for `chargeback|dispute` and `provider_reference` uniqueness it is **not** low risk. Recorded as `P06-OQ-94`.

**E2-C-03 — The two module registries you found are Odoo 19. You used them anyway.**
**Response — challenge answered.** They are used for exactly one purpose: to show that **no target-system registry exists** and to record what a comparable vendor-built database contains. `24_` labels every inference from them `SUPPORTED INTERPRETATION`, never `FACT VERIFIED`, and states outright that neither is the SMEsPlus target.
**But E2 adds something the package under-weighted:** those registries are **Odoo 19** while P06 researched **v18**. If the programme's target generation has moved, a material fraction of this package is scoped to a superseded line. **That is `P06-B-44`'s real severity, and it is understated.** Amendment: `B-44` re-worded to lead with the generation gap rather than the missing registry.

**E2-C-04 — `iso20022_uetr` — you say it has no inbound counterpart. Did you search the inbound models, or infer it?**
**Response — searched.** PATTERN `uetr` over `$V18E`, `*.py`: 22 hits, all in the outbound ISO 20022 path; none on `account.bank.statement.line`. And CAMT's inbound `EndToEndId` is written to `notes` (`camt/models/account_journal.py:127,130`), which is a positive demonstration rather than an absence. **Challenge answered.**

---

## Expert 3 — Lead Integration & Localization

**E3-C-01 — You closed `OQ-90` with two localisation packs. A real Odoo 18 has ninety. Is a 2-of-90 sample a closure?**
**Response — conceded on the framing, defended on the conclusion.** It is not a sample of 90; it is **the population of this build**, and the build is the deployment target. **The correct statement is: the negatives survive the localisation surface *of the system under study*.** They are not, and are not claimed to be, negatives about Odoo 18's localisation ecosystem.
**E3 does not accept that this fully disposes of the risk** — see `P06-OQ-94` — and that dissent is preserved.

**E3-C-02 — Thailand ships neither a bank-fee nor a returned-item concept, and you treat that as strengthening your finding. Could it instead mean the capability lives outside the ERP entirely?**
**Response — this is the best point raised in this challenge, and it is not answered.** Thai SMEs demonstrably incur bank charges and hold post-dated cheques. That the platform models neither may mean (a) the capability is missing, which is P06's reading, or (b) it is handled outside the system by convention, which would make it a **business-process** finding rather than a defect.
**P06 cannot distinguish these from source.** **Amendment:** `B-17` and `B-34` now carry this alternative reading explicitly. Recorded as `P06-OQ-95` — resolvable only by asking the business how they handle bank charges and PDCs today.
**This is a genuine widening of a finding's uncertainty and it is recorded as such.**

**E3-C-03 — The 2C2P and PromptPay findings rest on copies you cannot attribute. Why are they in the package at all?**
**Response — challenge answered.** They are byte-identical at the Python layer across copies (CMD-F-01), so behavioural findings hold for whichever is deployed. No deployment claim is made anywhere.

**E3-C-04 — P07 marks three dependencies on P06 as BLOCKING. You accepted all three and declared all three defective. Is that a handoff or an abdication?**
**Response — partially conceded.** Accepting ownership of a fact and then reporting it broken is honest but not helpful on its own. **Amendment:** `35_` §6 now states what P06 *will* supply — payment date, allocation and reversal linkage as **specified requirements** for the target — rather than only what the reference fails to supply. Recorded.

---

## Expert 4 — Lead Code & UI Architect

**E4-C-01 — `P06-B-50` (`om_data_remove`) is the most severe finding in the package and it arrived in an appendix. Is the severity ranking real?**
**Response — conceded.** It deletes the ledger, the chatter and the sequence position, by unconditional SQL, with a client-side confirm as its only gate, in all four custom roots. **It should not be an appendix item.** It is not ranked above the seven attack defects anywhere in the package.
**Amendment:** `B-50` is elevated in `43_` §6's severity list and in the handoff pack. Recorded.

**E4-C-02 — Your severity model is still absent. AAS+ said so last round and it is still absent.**
**Response — conceded, unchanged.** The prior round's AASP-F-04 recommended ranking by **precondition reachability** and that ranking was never built. This continuation added twelve blockers without ranking them either.
**This is a standing defect of the package, and it is now two rounds old.** `P06-B-41` is amended to carry it.

**E4-C-03 — `P06-B-51`: you claim an approval framework disables its own gate. That rests on a context flag set in one method and read in another. Have you traced an actual path?**
**Response — partially conceded.** The evidence is: `check_rule` returns `True` when `run_python_code` is in context (`multi_approval_type.py:692`), and the approve/refuse hooks set `run_python_code: 1` (`:616`) before `safe_eval(..., mode="exec")` (`:657-667`). **The flag and its reader are quoted; an end-to-end execution was not traced.**
**Amendment:** `B-51` re-classified from CONFIRMED DEFECT to **PLAUSIBLE — the bypass flag and its consumer are both quoted, but no executed path was traced.** Recorded as `P06-OQ-96`.
**This is a downgrade of a finding this continuation raised, and it is the correct call.**

**E4-C-04 — You corrected your own blocker arithmetic after publishing it. How many other counts in this continuation were published without execution?**
**Response — audited in response to this challenge.** Counts in this continuation and their provenance:
- 42 / 36 baseline — **executed** (`21_`)
- 54 / 39 current — **executed** (`40_`, after REV-E-06)
- 5 root-delegated fields — **read from source**, two files quoted
- 7 ingestion doors — carried from round 1, **not re-executed this round**
- 13 fee tokens, 11 identity tokens, 19,982 custom files — **executed by the evidence stream**, counts reported with commands
- 791 addon dirs, 2 l10n packs — **executed**
- 503 / 253 installed modules — **executed**
**One count is carried rather than re-executed: the 7 doors.** Recorded as `P06-OQ-97`. **The audit itself was prompted by challenge, not by the author.**

---

## Cross-cutting

**AAS-X-03 — Of the four risk classes you were told to test, which did this continuation actually fail on?**

| Risk class | Verdict |
|---|---|
| **False-positive closure** | **Low.** 4 blockers + 3 open items closed, each on quoted source. One closure (`B-51`) was **downgraded to PLAUSIBLE** by this challenge. |
| **Absence from incomplete population** | **REAL, and newly discovered.** `P06-B-55` — the evidence tree is a filtered distribution. Two experts raised it independently. |
| **Cross-process ownership** | **Moderate.** P06 absorbed a peer finding into its own register (`B-53`, now marked inherited) and accepted three BLOCKING dependencies. Deduplication at P11 is required. |
| **Financial integrity** | **Elevated by this round, not reduced.** `B-50` (ledger deletable by SQL with no server-side authorisation) and `B-52` (write-off producer with a blanket ACL) are both new and both material. |

---

## Amendments produced

| # | Amendment | Type |
|---|---|---|
| 1 | `25_` §4 relabelled `DESIGN CANDIDATE` | narrowing |
| 2 | `P06-B-53` marked *inherited from P05* for P11 deduplication | attribution |
| 3 | Tree-scope negatives inherit the filtered-build boundary (`P06-B-55`) | **scoping** |
| 4 | `P06-B-44` re-worded to lead with the **generation gap** (19 vs 18) | **severity up** |
| 5 | `B-17` / `B-34` carry the "handled outside the ERP" alternative reading (`OQ-95`) | **uncertainty widened** |
| 6 | `35_` §6 states what P06 will supply to P07, not only what fails | constructive |
| 7 | `P06-B-50` elevated in severity ordering | **severity up** |
| 8 | `P06-B-51` **CONFIRMED → PLAUSIBLE** (`OQ-96`) | **downgrade** |
| 9 | `P06-B-41` amended to carry the two-round-old missing severity model | standing defect |
| 10 | New open items `OQ-94`, `OQ-95`, `OQ-96`, `OQ-97` | new |

**Ten amendments: two severity increases, one downgrade, one uncertainty widening, one scoping correction.**

---

## Dissent preserved

| ID | Position | Counter-position | Status |
|---|---|---|---|
| `DIS-07` | The localisation closure is sufficient — the build is the target | E3: a 2-of-90 surface cannot close a capability question | **Both stand** — `OQ-94` |
| `DIS-08` | Missing bank-fee/PDC concepts are platform defects | E3: they may be handled outside the ERP by business convention | **Both stand** — `OQ-95` |
| `DIS-09` | `B-51` is a confirmed self-disabling gate | E4: no executed path traced | **E4 prevails** — downgraded to PLAUSIBLE |
| `DIS-10` | `25_` §4 is a semantic model | E1: it is a design proposal | **E1 prevails** — relabelled |
