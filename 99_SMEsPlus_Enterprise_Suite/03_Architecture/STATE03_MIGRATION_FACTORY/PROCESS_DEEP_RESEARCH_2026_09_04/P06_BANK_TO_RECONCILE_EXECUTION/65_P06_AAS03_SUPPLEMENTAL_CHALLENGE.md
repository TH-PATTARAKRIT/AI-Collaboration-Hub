# P06_AAS03_SUPPLEMENTAL_CHALLENGE.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S20)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Mandate:** four experts, fresh challenge. **Four adversarial attempts are compulsory** and are executed in §5.

---

## Expert 1 — Leader Functional Design

**E1-S-01 — You raised the copy count from 4 to 17 and called it "materially understated". Did the finding change, or only the number?**
**Response — the finding changed.** Four copies in four declared roots reads as vendor baggage. **Seventeen copies across four Odoo generations, seven at the installed version, and three rebranded `SMEsPlus Remove Data` — two of them inside this programme's own account workspace — reads as adoption.** A module nobody uses does not get renamed after the project.

**E1-S-02 — `46_` puts `B-06` in a CRITICAL row of its own, off the reachability grid. Is that not a device to keep a favourite finding at the top?**
**Response — a fair suspicion, and the test is whether it earns the place.** `B-06` has no precondition because it is not an event; it is the permanent absence of a fact. Placing it in R1 would imply a trigger it does not have; omitting it would hide the deepest finding. **The row is annotated, not hidden, so a reader can disagree.** E1 accepts the placement and records that the device is only legitimate because it is declared.

**E1-S-03 — `61_` says the sequence rewind is "largely inert", then says the situation is worse. Both cannot be true.**
**Response — both are true and the challenge is right that the file must say so plainly.** The `ALTER SEQUENCE` is largely inert **against v18 journal numbering**. The renumbering happens anyway, **by a different mechanism** — emptying the table the numbering reads. **The correction moves the cause, not the effect.** It is worse because protecting `ir.sequence` would not prevent it. **Amendment: `61_` §3 to state the two clauses adjacently.** Recorded.

**E1-S-04 — P08 claimed `F-06` and `F-17`. You accepted both immediately. Did you verify their claims or just take them?**
**Response — partially conceded.** P06 verified that P08 *claims* them (quoted owned rows) and that P08 supplies substantive findings behind each (`JPM-02` two posting doors; `PC-17` no close object). **P06 did not independently verify `JPM-02` or `PC-17` against source.** They are cited as P08's findings, which is correct attribution, but P06 has adopted a conclusion it did not test. Recorded as `P06-OQ-118`.

---

## Expert 2 — Leadership Database Design

**E2-S-01 — The FK census is the strongest new evidence and it is entirely second-hand. Did you read `fields.py:3189-3197` yourself?**
**Response — conceded, and it matters.** The ORM default-resolution rule and the FK counts come from an evidence stream, not from this session's own reading. **The rule is quoted verbatim and is checkable in seconds; the counts across 9,431 files are not.**
**Amendment: `59_` §4 carries a provenance note** — the resolution rule is quoted and verifiable; the per-table counts are single-source and unverified by a second pass. `P06-OQ-119`.

**E2-S-02 — You claim `account_full_reconcile` rows survive orphaned. Is that a database fact or an inference?**
**Response — challenge answered.** Both inbound references are `Many2one` with no `ondelete`, non-required, non-transient → `SET NULL` by the quoted rule, and **both point partial→full and line→full**, never full→partial. The inverse links are `One2many`, which have no database column. **Deleting partials cannot touch full-reconcile rows. That is topology, not inference.**

**E2-S-03 — `remove_account_chart` deletes `res.partner.bank` first, and you say three RESTRICTs refuse it. So the method fails immediately and does nothing?**
**Response — no, and this is the sharpest consequence in the file.** The refusal is **swallowed to a warning** and the loop **continues**. So the method fails at step 1 and proceeds to delete the chart of accounts and the journals at steps 10 and 11. **Partial destruction is the normal outcome.** `59_` DPG-F-04.

**E2-S-04 — Registry evidence: you found `om_data_remove` installed on `iEVING`, a BHPRO database. You then upgraded a P06 severity on it. Is that legitimate?**
**Response — partially conceded, and the wording has been policed.** `58_` states plainly that `iEVING` is **not confirmed to be the SMEsPlus target**, and `49_` labels the upgrade *"on a v19 database not confirmed to be the SMEsPlus target"*. **What the evidence does establish is that this module is not hypothetical in this estate: the same vendor, the same programme, installs it.** `46_` keeps `B-50` at R5 (unverified) rather than promoting it to R1. **E2 accepts the handling and notes it would have objected to any promotion of reachability band.**

---

## Expert 3 — Lead Integration & Localization

**E3-S-01 — Last round I said a 2-of-90 localisation surface cannot close a capability question. You then found 904 more packs you had not searched. Does that not prove my point entirely?**
**Response — conceded without qualification. E3 was right and the package was wrong.** Round 3 asserted a "filtered distribution" and used it to *bound* negatives; the localisations were sitting in `addons_archive` on the same disk, reachable, unsearched. **`P06-B-55` as published was substantially wrong** (REV-E-16).
**And the archive has now been searched**, which is the only acceptable response: one real field hit (`commission_amount` in an archived marketplace connector), no bank-fee concept, no returned-item concept. **`B-17`, `B-34`, `B-35` survive the enlarged population.**
**E3 records that the correction was produced by the challenge process, not by the author, for the second round running.**

**E3-S-02 — `l10n_th` is on the live path and 904 others are archived. Is that a filter, or a deployment choice?**
**Response — a deliberate deployment choice, and the distinction matters.** The project's own `odoo.conf:14` states `addons_archive` must not be on the `addons_path`. **Nothing was lost; a boundary was configured.** The word "filtered" implied loss and was wrong. `56_` FTB-F-01 rewritten.

**E3-S-03 — v19 ships `l10n_account_withholding_tax`. You routed it to P07 and moved on. Is that not exactly the cross-version risk you claim to have retired?**
**Response — conceded in part.** `51_` claims cross-version invariance for **six core findings**, and every one was re-tested. **It does not claim invariance for the Thai WHT domain**, and the native v19 module is recorded as **VERSION-DEPENDENT**. But the challenge lands on emphasis: **if the target is v19, the two custom WHT subsystems P05/P06/P07 all found are competing with a platform capability**, and that is a live risk P06 mentions once and does not weigh. **Amendment: raised to the P11 handoff as a named item, not a footnote.** Recorded.

**E3-S-04 — Three copies are rebranded with the project's name. You call that "adoption". Could it not be a vendor's white-labelling?**
**Response — genuine alternative, not disposed of.** The manifest `author` remains `Odoo Mates, Sunpop.cn` in every copy; only `name` changes to `SMEsPlus Remove Data`. **That is consistent with white-labelling by whoever assembled the distribution, which may be the vendor rather than this programme.** `58_` DMR-F-06 states the fact and infers adoption; **the inference is downgraded to `SUPPORTED INTERPRETATION` and the alternative recorded.** `P06-OQ-115`.

---

## Expert 4 — Lead Code & UI Architect

**E4-S-01 — Last round I raised the missing severity model. You built it. Does it survive its own criteria?**
**Response — tested, and one assignment is arguable.** `B-10` (duplicate ingestion) qualifies on **C5** systemic duplicate financial effect — defensible: re-importing a CSV creates duplicate posted entries silently. `B-13` (identity mutable without trace) qualifies on **C4** irrecoverable audit-lineage loss — **weaker**, because the identity fields are not themselves the audit trail. **E4 challenges `B-13`'s CRITICAL placement.**
**Response accepted in part:** `B-13` is retained CRITICAL because a bank event whose identity can be changed without trace **cannot be reconciled to its source afterwards**, which is lineage loss in substance. **But it is the weakest of the six and is marked as such.** Recorded.

**E4-S-02 — You downgraded `B-51` to PLAUSIBLE last round for lack of a traced path. `B-50`'s authorisation claim is also untraced by execution. Why is one CONFIRMED and the other PLAUSIBLE?**
**Response — the distinction is real and worth stating.** `B-51` required inferring that a flag set in one method reaches a check in another **through an execution path nobody traced**. `B-50`'s chain is **four quoted links in a fixed dispatch sequence** — route, `get_public_method`, `call_kw`, method body — each read in full, with **no branch between them**. **One is a hypothesis about control flow; the other is a reading of a straight line.** E4 accepts the distinction.

**E4-S-03 — `44_` says the copies are "NOT identical" and corrects the prior round. But CUST18 ≡ T8MASTER byte-for-byte. Is the correction overstated?**
**Response — narrowed.** Two of four are identical; MIGR18 and CUST14 differ materially. **The correct statement is "three distinct variants across four copies", not "the four copies are not identical".** Amendment applied to `44_` OMD-F-01. Recorded.

**E4-S-04 — Sixteen author errors across four rounds. At what point does the error rate itself become the finding?**
**Response — it already is, and the package says so.** `62_` §"The recurring defect, named once": ten of sixteen are one defect — a boundary drawn and not stated, or stated and not executed. **Twelve of sixteen were caught by something other than the author.**
**E4's sharper point stands and is recorded as a standing risk:** a package that corrects itself this often is either unusually honest or unusually unreliable, **and the evidence cannot distinguish those from inside the package.** Only an independent audit can. `P06-B-58`.

---

## 5. The four compulsory adversarial attempts

**ADV-1 — Attempt to DISPROVE: *"om_data_remove has no server-side authorization."***
**Attack:** find any enforcement the trace missed. Candidates tested: the model ACL (`base.group_system`, `unlink=0`) — **not invoked**, no ORM call on the model; the menu `groups=` — **client-side**; the action — **no `groups` field**; `get_public_method` — blocks only `_`-prefixed, `@api.private`, `_UNSAFE_ATTRIBUTES` and class/staticmethods, **none of which applies**; `call_kw` — **no access check**; record rules — apply to `search`/`read`, **neither occurs**; a module `security/` file — **absent in all copies checked**.
**Result: NOT DISPROVED.** One unexamined mitigation remains: **Postgres role separation** would refuse the `DELETE` — and the refusal would be **swallowed to a warning**. `P06-OQ-102`, **HOLD — DEPLOYMENT EVIDENCE REQUIRED**.

**ADV-2 — Attempt to DISPROVE: *"the destructive operation can affect posted financial history."***
**Attack:** find a guard that protects posted records. Candidates: posted state is a **column**, and SQL does not read columns it does not name; `_check_reconciliation` and the audit-trail guard live in `unlink()`, **not reached**; the inalterability hash is checked in `write()`/`unlink()`, **not reached**; lock dates are checked in ORM paths, **not reached**; FK `RESTRICT` **does** refuse some tables — **but `account_move` has zero restricts and five cascades**, so journal entries and their lines go.
**Result: NOT DISPROVED, and partially strengthened** — the only real obstacle found (RESTRICT) protects `res_partner_bank`, `account_journal` and `account_account`, **not the transactional history**.

**ADV-3 — Attempt to DISPROVE: *"the v19 deployment evidence cannot safely establish v18 deployed behavior."***
**Attack:** show that v19 evidence transfers. **This one partially SUCCEEDS.** Six core P06 findings were re-tested against the complete v19 tree and are **cross-version invariant** (`51_` §2) — `is_matched`, `root_id` delegation, the reconcile lock-date absence, `remove_move_reconcile`, the fee absence, and the RPC dispatch chain. **For those six, v19 evidence does transfer.**
**But it fails for the rest.** The FK census, the `ir.sequence`/`sequence.mixin` analysis and the `account.full.reconcile` topology were derived **only** against v18 and **not re-run** against v19 (`P06-OQ-116`, `P06-OQ-117`) — while `iEVING` is v19. **Refined conclusion: v19 evidence establishes the six re-tested invariants and nothing else. The proposition is DISPROVED in part and stands in part**, and the package must say which.

**ADV-4 — Challenge the CRITICAL severity assignment.**
**Attack on `B-50`:** it is CRITICAL only if reachable; reachability is `SOURCE-REACHABLE` on v18 and `DEPLOYMENT VERIFIED` on a database that is **not the target**. **A CRITICAL that may not apply to the target is a category error.**
**Response — partially conceded, and the heatmap already handles it.** `47_` places `B-50` at **R5 — unverified**, not R1. Its severity is impact-based (C1, C2, C4, C6) and its reachability is separately and honestly low-confidence. **The two-axis model exists precisely so this challenge can be answered without moving the letter.**
**But E4's underlying point is accepted:** if `om_data_remove` is proven absent from the SMEsPlus target, `B-50` becomes a **latent supply-chain risk**, not a live CRITICAL — and `58_` §6 names the query that would settle it. **The severity is conditional and is now marked conditional.**

---

## 6. Amendments produced

| # | Amendment | Type |
|---|---|---|
| 1 | `61_` §3 states the "inert mechanism / real damage" clauses adjacently | clarity |
| 2 | `59_` §4 carries a provenance note — FK counts are single-source | **evidence honesty** |
| 3 | `44_` OMD-F-01 narrowed to "three distinct variants across four copies" | **narrowing** |
| 4 | `58_` DMR-F-06 rebranding inference downgraded to `SUPPORTED INTERPRETATION`; white-labelling alternative recorded | **downgrade** |
| 5 | v19 native WHT raised to the P11 handoff as a named item | escalation |
| 6 | `B-13` retained CRITICAL but marked the weakest of the six | qualification |
| 7 | `B-50` severity marked **conditional** on target installation | **qualification** |
| 8 | ADV-3 conclusion refined: v19 transfers for six re-tested findings only | **scoping** |
| 9 | New: `P06-B-58` — the package's own correction rate as a standing reliance risk | **new blocker against itself** |
| 10 | New open items `OQ-115` (rebranding), `OQ-118` (P08 claims unverified), `OQ-119` (FK census single-source) | new |

**Ten amendments: three downgrades or qualifications, one new blocker raised against the package itself, one conceded-in-full.**

---

## 7. Dissent preserved

| ID | Position | Counter | Status |
|---|---|---|---|
| `DIS-12` | The rebranding indicates programme adoption | It may be vendor white-labelling — `author` is unchanged | **Both stand** — `OQ-115` |
| `DIS-13` | `B-13` is CRITICAL (lineage loss) | Identity fields are not the audit trail | **Retained, marked weakest** |
| `DIS-14` | `B-50` is CRITICAL | Conditional on target installation | **Retained, marked conditional** |
| `DIS-15` | v19 evidence transfers | Only for the six re-tested findings | **Refined, both recorded** |
| `DIS-16` | The package's self-correction is a strength | It cannot be distinguished from unreliability from inside | **Unresolved — `P06-B-58`** |
