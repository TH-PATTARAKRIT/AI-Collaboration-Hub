# P06_AAS_PLUS_CONSOLIDATION.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G08)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Consolidates:** `P06_AAS03_BOUNDED_CHALLENGE.md`. **Standing vetoes carried from `42_`, `66_`, `67_` are re-tested, not re-asserted.**

---

## 1. What the challenge actually did

**Sixteen expert findings were raised. Six were executable inside this round's bound and were executed. Every one of the six changed the result.** That is the argument for the challenge step, stated as an outcome rather than as a principle.

| Expert finding | Executed? | **Outcome** |
|---|---|---|
| `E1-G-02` — a reversal-type taxonomy built on two values when more producers exist | **YES** — `SL-G-19` | **UPHELD. Seven producers, not two.** And two of the seven — `account_full_reconcile.py:34`, `account_partial_reconcile.py:133` — **are P06's own unreconcile primitives.** `P06-B-59` is not only about foreign objects entering P06's population; **P06 manufactures the same ambiguity itself** (`SL-F-02`) |
| `E2-G-02` — the `account.reconcile` value was determinable and was not determined | **YES** — `SL-G-20` | **UPHELD, and the payoff exceeded the challenge.** 40 of 40 `liability_current` and 15 of 23 `asset_current` accounts are reconcilable on `iEVING`. **And the deferred *expense* account is configured as the BANK SUSPENSE ACCOUNT** — `P06-B-61`, CRITICAL |
| `E4-G-01` — `P06-B-59` is proven for the batch wizard and assumed for the widget | **YES** — `SL-G-15`, `SL-G-16` | **UPHELD as a challenge; the finding SURVIVES.** `bank_rec_widget.py` is 1,780 lines and contains **zero** occurrences of `reversed_entry_id`; its candidate domain admits an unreconciled posted pair. **Both engines. And a new observation fell out: the domain mixes `root_id`-scoped accounts with `company_id`-scoped lines** (`SL-G-17`) |
| `E4-G-02` — the zero-balance strategy was quoted and not analysed | **YES** — `SL-G-13` | **UPHELD.** `groupby [account_id, partner_id, currency_id] having sum = 0`, **no amount key at all.** Strictly wider than the strategy the finding was built on |
| `E3-G-04` — two undeclared trees in two rounds is a trend | **YES** — `SL-G-21` | **UPHELD, decisively. Sixteen distribution roots exist; the package researched two.** Run under two independent patterns because either alone produced a false negative |
| `E4-G-04` — `REV-E-21`'s denominator is half the population | **YES** — `REV-E-21` §5 | **UPHELD, and it CHANGED the finding.** Rounds 1–2 scored **7 of 7**; round 4 scored **2 of 8**. *"Systematic"* is **withdrawn**; the accurate finding is **a volume failure in one round** |
| `E2-G-03` — `PDR-F-06`'s restraint on `mail.message` was misapplied | **partially** | **UPHELD.** Pursuing it produced `IEV-F-03` — **44 orphaned chatter rows across five emptied transactional models**, the discriminating evidence in the `iEVING` forensic. **The restraint would have suppressed the round's strongest finding** |
| `E1-G-01` — the business truth of partial/full is never stated | no | **CONCEDED, unresolved.** `CQ-P06-03` answers mechanically. Carried as `P06-OQ-126` |
| `E1-G-03` — `B-59` is filed as a matching defect and is a semantic one | no | **CONCEDED in part.** Recorded in `P06-B-59`'s statement; the layer question is a PHASE B decision, not a PHASE S one |
| `E1-G-04` — `PDR-F-05` defends its own judgement | no | **CONCEDED. The self-assessment is not evidence** and is now labelled as an author's note rather than a finding |
| `E2-G-01` — no index analysis | **YES** — `SL-G-10` | **CLOSED.** `index='btree_not_null'`. A reversal-aware predicate is affordable |
| `E2-G-04` — three-build invariance is not three independent tests | no | **UPHELD as a limitation.** Identical line numbers across two v19 builds indicate the same upstream code. **The claim is restated as *version-drift-bounded*, not *independently confirmed*** |
| `E3-G-01` — no route exists to deliver `HO-03` to P10 | no | **UPHELD and UNRESOLVED. This is the round's sharpest unresolved item** — see §3 |
| `E3-G-02` — the Thai localisation dimension is absent | partially | **PARTIALLY ANSWERED by accident:** `SL-G-20` read a **Thai chart of accounts**, and it is the one that marks 40 of 40 accrual-type accounts reconcilable. **The l10n packs themselves were still not consulted.** `P06-OQ-127` |
| `E3-G-03` — reading P10's *"Do not start P06"* as internal to P10 | no | **CONCEDED as an interpretation.** Recorded, not resolved |
| `E4-G-03` — 30 self-applied unreviewed edits cited as evidence of integrity is circular | no | **UPHELD. This is the veto item** — see §4 |

## 2. Findings raised or changed by consolidation

| ID | Statement | Severity | Class |
|---|---|---|---|
| **`P06-B-59`** | Neither reconciliation engine — the auto-reconcile wizard nor the bank-rec widget — can distinguish a structural reversal pair from a corrective one. `reversed_entry_id` is the only link, it carries no type, and **zero of two engines read it**. **Seven producers write it; two leave the pair unreconciled and in the matching population** | **HIGH** | `FACT VERIFIED` (source) · **`REACHABLE — CONFIGURATION VERIFIED` on `iEVING`** |
| **`P06-B-60`** | The company deferral account is partner-attributed and may be reconcilable, admitting deferral moves into P06's population | **superseded by `P06-B-61`** | merged |
| **`P06-B-61`** | **On the deployed `iEVING` database both companies configure `deferred_expense_account_id` = account 3 = the BANK SUSPENSE ACCOUNT, `reconcile = TRUE`, with `generate_deferred_expense_entries_method = on_validation`.** Every deferral entry would post into the same reconcilable account as every unmatched bank event | **CRITICAL** — `C5`, `C6` | configuration `FACT VERIFIED`; consequence `SUPPORTED INTERPRETATION`; **never fired here — `account_move_deferred_rel` = 0 rows** |
| **`P06-B-62`** | The bank-rec widget's candidate domain scopes eligible **accounts** by `company_id.root_id` — the fiscal hierarchy — while scoping eligible **lines** by `company_id`. **Third instance of the A4a root-scoping shape** after `P06-B-43` and `P06-B-27` | **HIGH** | `FACT VERIFIED` (`SL-G-17`) |
| **`P06-B-55`** | **RESTATED.** *The evidence base is 2 of 16 enumerated distribution roots.* Was: *"a filtered distribution"* — itself already corrected once to *"a relocation"* | unchanged | `FACT VERIFIED`, and the boundary is now a **number** |
| **`P06-B-50`** | **Evidential basis transformed.** Was: installed, with a manifest docstring as the only evidence of execution. Now: **a database in this programme's own evidence is in the post-execution state, on four independent observations, with three competing hypotheses tested and contradicted** | unchanged **CRITICAL** | see `P06_IEVING_LEDGER_STATE_FORENSIC.md` |

## 3. `AASP-VETO-06` — a P06 finding that has no route to its owner

**`E3-G-01`, upheld and unresolved.**

P06 has established that P10's mechanism, as configured on the one deployed database in evidence, would deposit deferral entries **into P06's bank suspense account**, and that P06's two matching engines cannot distinguish the resulting pairs from corrections. **P10 does not know this.** And `REV-E-18` is proof, in this same round, that **P06's previous outbound answer to P10 sat unreceived across two rounds and a commit.**

**VETO:** *No P06 handoff element that depends on a peer receiving it may be recorded as delivered on the strength of having been written into a P06 file.* `HO-03` and `HO-04` are **WRITTEN, NOT DELIVERED**, and are labelled so.

**Condition to lift:** a delivery mechanism that produces evidence of receipt — a peer commit, a Boss routing decision, or a P11 consolidation that both parties read. **This is not P06's to build.** `BOSS DECISION REQUIRED`.

## 4. `AASP-VETO-07` — the round repaired itself and cannot certify the repair

**`E4-G-03`, upheld.**

This round found that **6 of 15** prior corrections were never applied to the registers that carried the errors, and then applied **30 corrections across 15 register files in a single pass, authored by the party that made both the original errors and the repairs, with no independent verification.**

The package's own standing position — recorded since round 2 and confirmed again this round, where **zero of five** author errors were found by the author re-reading their own work — is that self-review is the weakest available control.

**VETO:** *P06 may not assert its own evidence integrity on the basis of corrections it applied to itself in the same round it discovered the defect.* Terminal state **A** is unavailable while this veto stands.

**Condition to lift:** an independent pass over the 30 edits, verifying that each superseded statement is quoted verbatim, each correction is accurate, and no correction introduced a new error. **The edits are individually greppable and the check is cheap; it is the independence that is missing, not the effort.**

## 5. Standing vetoes, re-tested

| Veto | Origin | Status after this round |
|---|---|---|
| `AASP-VETO-01` | no settlement/reconciliation design may proceed while `P06-B-50` stands | **UPHELD, and strengthened.** The `iEVING` forensic moves `B-50` from *"installed, possibly fired"* to *"installed, and a database in evidence is in the post-execution state"* |
| `AASP-VETO-02` | bank-confirmation semantics must be designed, not inherited | **UPHELD, untouched.** `P06-B-06` unchanged |
| `AASP-VETO-03` | tree-scope negatives inherit the evidence-base boundary | **UPHELD, and the boundary is now quantified: 2 of 16** (`SL-G-21`). The veto was right for four rounds and could not be discharged because nobody had counted |
| `AASP-VETO-04` | duplicate-ingestion controls must be designed before any import path | **UPHELD, untouched** |
| `AASP-VETO-05` | the package's correction rate is itself a risk to reliance | **UPHELD, and it is the veto this round vindicated.** Five new author errors, **zero** self-found by re-reading |
| **`AASP-VETO-06`** | **NEW** — no handoff is delivered by being written | **RAISED** |
| **`AASP-VETO-07`** | **NEW** — no self-certification of self-applied corrections | **RAISED** |

## 6. Consolidated position

**What this round established, on P06's own evidence:**
1. The settlement→recognition interface is **empty**, and empty by design (`BR-01`).
2. P06 reconciles **invoiced** value (`BR-02`).
3. The accrual has **no structured link** to anything (`BR-03`).
4. **Neither** matching engine can distinguish a structural reversal from a correction, and **seven** producers write the field neither reads — **two of them P06's own** (`BR-04`, `SL-F-01`, `SL-F-02`).
5. On the one deployed database in evidence, the accrual accounts are reconcilable and **the deferred expense account is the bank suspense account** (`SL-F-03`, `SL-F-04`).
6. That database's **entire transactional ledger is empty, with an ORM-impossible reconcile remnant and 44 orphaned chatter rows** (`IEV-F-01` … `IEV-F-04`).

**What this round could not establish:** whether any of it is true of the SMEsPlus target. `P06-OQ-98` is unchanged and remains the package's single most valuable open item.

**AAS+ does not declare PASS or FAIL and does not select the terminal state.** It records that **two new vetoes stand**, that **terminal state A is unavailable** while `AASP-VETO-07` stands, and that the choice between **B** and **C** turns on a question AAS+ puts to PMO rather than settling: *does a round that discovers an integrity failure, quantifies it, and repairs it in the same unreviewed pass thereby discharge it?*
