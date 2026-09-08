# P11 — CORR3 RE-CONVERGENCE AND FALSIFICATION PASS

`[SMEPLUS-26-09-06-…-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-05`/`-06` · **PHASE S** · AI EOS **OFF**

> Run **only after** intake integrity was established (`P11_CORR3_INTAKE_INTEGRITY_AND_DENOMINATOR.md`).
> **§11 discipline: for every load-bearing claim, P11 attempts to DISPROVE it before carrying it.**

---

## 1. Falsification pass

| # | Claim | Supporting evidence | Counterexample sought | Counterexample **found** | Resolution | Residual risk |
|---|---|---|---|---|---|---|
| `F-01` | **The settlement graph is reconcilable** (`CI-02`) | 63,773 records / 100,580 lines, residual drift 0 at tolerance ≥ 1e-6 | a mechanism that removes settlement rows outside the object layer | **YES — `P08-CONTRA-55`/`P08-HO-13`** | ~~Claim WITHDRAWN. P08 withdraws it against its own package~~ **CORRECTED (`X3-C6`): P08 did NOT withdraw it.** §1 item 2 still stands **unstruck** as `CANDIDATE OUTPUT`; P08 uses *"WITHDRAWN"* precisely for `P08-CONTRA-73` and `-57` and does **not** use it here. **What P08 states is a consequence against the claim, not an owner withdrawal.** P11 upgraded a consequence into a withdrawal | **`exercised` is `SUPPORTED INTERPRETATION`, not `NOT ESTABLISHED`** — `P06` `70_` L27, two rows below the line P11 quoted |
| `F-02` | **The ledger is arithmetically sound — ~~0 unbalanced across 169,143~~ → 0 unbalanced across the FOUR FROZEN RC-05 EXTRACTS (169,143 + 16 + 6 + 5)** **[`P11-C6-02`, 2026-09-08 — premise re-pointed to P08 `f0cf287ac9f4ad37b0c19145df4a0e396af84c13`; three-DB premise preserved as lineage; deployment completeness still UNPROVEN]** | `P08` §1 item 1, at `f0cf287ac9f4ad37b0c19145df4a0e396af84c13` | a tolerance at which the count is non-zero | ~~**YES** … *"at 1e-7 the answer is 3"*~~ → **NO. WITHDRAWN `2026-09-07` (`Q-P11-04` / `XRD-011`).** **The figure has no referent.** `P08`'s independent verifier re-derived it **in exact `Decimal`: 0 unbalanced at `0.005`, at `1e-4`, at `1e-7` AND at exact equality**, on both the computed and the stored balance (`P08_INDEPENDENT_AAS03_CHALLENGE.md` §2.3, *"A figure with no referent, shipped to P11"*). **There is no tolerance at which the count is non-zero.** Received and attributed; **P11 did not and may not re-derive P08's balances** (`Q-P08-01` owns that) | **`F-02` YIELDS NO COUNTEREXAMPLE.** The correct answer to its own question is **NO**. The claim stands as *0 unbalanced in the reporting currency across 169,143, at every tolerance tested including exact equality*. **The word *"complete"* remains withdrawn on separate grounds** (`P08-CONTRA-73` — the deletion path), which is unaffected | **P11 consumed a peer figure, answered its own falsification `YES` on it, and derived a standing method rule from it. See the rule's re-grounding below** |
| `F-03` | **96.1 % of posted entries carry an origin pointer** | `P08` §1 item 5 (CORR2) | a stricter predicate for *origin pointer* | **YES — `P08-CONTRA-63`.** **78.03 %** carry a **structured** pointer; 96.1 % counted **free-text reference**. **~30,750 entries' only provenance is unparsed text** | **Corrected to 78.03 %** | P08 records the figure moved **12.7× down then 5.6× up** across two rounds, *"both from predicate error"* |
| `F-04` | **There is no accounting period to reconcile within** (`T0-15`) | `P08` `A VERIFIED ABSENCE`; 0 of 6 companies close; no lock date on 3 surfaces | a period-like object in **another generation** | **YES — `P08-CONTRA-68`.** Absent **in the declared 18.0 root set only**. *"The 19.0 line carries a dated, recurring return object, and both 19.0 deployed databases carry its linking column on the entry table"* | **`T0-15` RE-SCOPED to the 18.0 source line.** P08's instruction quoted: ***"P11 must not receive the absolute"*** | A tax return is not a general accounting period; the 19.0 object's accounting sufficiency is untested |
| `F-05` | **Settlement chronology is untrustworthy — 46.4 % after / 44.3 % before as-of date** (`CQ-P11-04`) | `P08` §2 item 5 (CORR2) | that the two dates are not comparable | **YES — `P08-CONTRA-57`.** The as-of date is **computed by the kernel** as the later of the two items' accounting dates; the split compared a **write timestamp** against a **derived date** and *"**contains no defect**"* | **WITHDRAWN.** P11 carried a non-defect as a finding for one round | `CQ-P11-04`'s *"four distinct times"* loses its strongest support |
| `F-06` | **`฿29,029,467.66` is the largest unrecognised accounting position** (`B-28`, CORR2) | `P01` §6 | the owner's own classification | **YES.** *"**This is a timing position, not a missing transaction** … under periodic valuation no receipt-time entry is expected … **P08's judgement and the Boss's decision**"* | **Framing WITHDRAWN.** Carried as `CANDIDATE INPUT — NOT PROMOTED`. **`฿1,538,601.86` of it is operator-typed with no receipt document and must not be read as received** | The completeness question at a reporting date is real and is **not P11's to answer** |
| `F-07` | **`P11-C-12`** | `P08` kernel; P11's `0 of 7 unqualified` | a case where the party-dimension identity fails | **YES — and P11 missed the strongest one, which it already held (`X1-9`/`X3-C7`): `P03`'s `73_` §3B — *"**25 mismatched, 0 matched. The inventory subsidiary ledger and the general ledger have diverged**"*, a measured divergence on a genuinely separate store, immune to the *true-by-construction* defence and already `FACT VERIFIED` in P11's own matrix.** Plus: `P01`: **10 of 1,904** vendor bills balance to a non-payable account — *"a payables ageing scoped to the payable account type **will not see these liabilities**"*. And **`P08-U-28`**: *"every kernel claim in this handoff rests on the 18.0 line. **No deployed database runs it**"* | **Downgraded to `SUPPORTED INTERPRETATION — 18.0 SOURCE LINE`** and carried under `AAS+-VETO-01` | The claim may not be true of **any** deployed generation. It was P11's headline for one round |
| `F-08` | **`P11-C-15`** | `P02` `43_` §5 | that one relayed it from the other | **YES — and P11 published the opposite.** `P10_G02_SOURCE_LINK_REGISTER` L14: *"**P02 authoritative closure `7cb1c27` … Consumed as controlled input**"*; L24 files the invariant finding as **admitted P02 evidence**; `P10_TO_P11_HANDOFF` L55 **credits the correction/reversal location to P02**. And P10 marks `G02-E-C` (design candidates) *"reached independently"* while attaching **no** independence claim to the invariant — **P11 demoted the independent item and promoted the relayed one** | **CONVERGENCE LABEL WITHDRAWN.** One finding (`P02`), one post-hoc concurrence (`P10`). **`P11-C-09` repeated in the round that corrected it** — `P11-E-43` | P11 relayed P10's word *"independently"* without testing it, **and did not open P10 this round** |
| `F-09` | **`B-21`/`T0-14` — deletion path installed** | `P01` series-16 + FK; `P06` v19 non-target; `P08` `P08-HO-13` | that it is confined to one non-target database | **NO — it is WIDER** | **STRENGTHENED, and the ladder rung CORRECTED (`X1-2`, `X4-R5`).** ~~exercised NOT ESTABLISHED~~ → **`exercised` = `SUPPORTED INTERPRETATION`** (`P06` `70_` L27: *"Execution having occurred \| **SUPPORTED INTERPRETATION** — first-party remediation module, not a log"*). **P11 wrote NOT ESTABLISHED three times, routed the answered question to P06 as an open ask, and counted its non-delivery as evidence for `B-31`** | **`installed` itself is a P08 row, and `P08-U-28` makes every row of that file an 18.0 statement.** Under P11's own `B-33` the defensible rung for `T0-14`/`T0-16` is **source present**, not **installed** |
| `F-10` | **`B-26` — the deletion explanation covers the valuation-layer zeros** | `ON DELETE SET NULL` + installed module | a zero the mechanism cannot produce | **Already found at CORR2** (3 of 6 incoherent). **Sought again against `P08-HO-13`'s wider table set** — settlement, items, entries | **Bounded held**, and **widened to the settlement graph** (`F-01`) | The universal stays withdrawn |

**10 claims tested. 9 counterexamples found.**

| Disposition | Count | Rows |
|---|---|---|
| withdrawn / re-scoped / corrected / downgraded | **7** | `F-01` … `F-07` |
| strengthened, rung corrected | **1** | `F-09` |
| **convergence label withdrawn** | **1** | `F-08` |
| bounded, held | **1** | `F-10` |

**CORRECTED (`X2-C11`/`X4-C9`): the published tally `5 + 1 + 1` covered 7 of 10 and undercounted P11's
own self-correction by 2.** `F-08` moved from *survived* to *withdrawn* on the challenge.

> ### `P11-F-16` — **the falsification pass disproved more of P11's own carried claims than the four-expert challenge did.**
> Every one of `F-01` … `F-06` was disproved **by the owner's own current statement**, sitting in the
> frozen snapshot, requiring no new research — only reading the artefact at the head P11 had already
> resolved. **Attempting disproof first is cheaper than being corrected, and it found more.**

---

## 1b. The method rule derived from `F-02` — **WITHDRAWN**

`P11_ACCOUNTING_TRUTH_CONVERGENCE_MATRIX` and `F-02` carried a standing rule:

> ~~**"A soundness claim without a tolerance is not a claim."**~~

**It was derived from exactly one instance — *"at 1e-7 the answer is 3"* — and that instance has no
referent.** P08's independent verifier found **0 at every tolerance including exact equality**. The
observation that generated the rule never happened.

> ### **The rule is WITHDRAWN, not re-grounded.**
>
> It may well be sound on other grounds. **P11 has not established those grounds and will not assert
> them.** A rule that survives only because it sounds right is a rule with no evidence, and this
> package has spent four rounds learning that **plausibility is not evidence**. Preserved as
> `CANDIDATE METHOD RULE — UNGROUNDED`, available to any party that can evidence it independently.

**What this instance *does* support, and it is the opposite lesson:**

> ### `P11-G-09` — **a consumer that adopts a producer's figure inherits the producer's measurement error, and a method rule derived from a single unverified figure inherits it twice.**
>
> P11 took `"3"` from a peer handoff, **answered its own falsification `YES` on it**, and promoted the
> result to a standing rule governing every future soundness claim. **Three artefacts deep, none of
> them re-derived.** The correct handling of a producer's figure that is load-bearing for a P11 *rule*
> — as distinct from a P11 *record* — is to require the producer's own verification of it first.
>
> **P11 could not have caught this alone**: re-deriving P08's balances is `Q-P08-01`'s work and is
> forbidden to P11. **The control that caught it was structural independence at the producer.**

## 2. Re-convergence — the 16 challenge axes, applied to what survives

| Axis | Position after falsification |
|---|---|
| **1 Business fact / event identity** | Absent as a platform property; **`P02` independently requires it** (`IC-02`). Class `C`. `D-5` |
| **2 Producer / source owner** | Per `CI-01`…`CI-12`, all attributed |
| **3 Operational truth owner** | Peer-owned; P11 takes **reliance only** (`P11-G-06`) |
| **4 Accounting truth owner** | **Unowned for the two tie-outs** (`OC-01`, `OC-02`) |
| **5 Occurred/effective/recognition/posting/settlement** | **Weakened** — `F-05` removed the chronology finding. What survives: recognition collapsed into posting (`P10`), and `฿29.0m` received with **no recognition of any kind** (`IC-01`) |
| **6 Debit/credit** | **30 producer cells remain WITHHELD.** `P01`'s *"FALSE IN BOTH HALVES"* stands as the reason |
| **7 Subledger ↔ GL** | `P11-C-12` **downgraded to an 18.0-source-line interpretation** (`F-07`) |
| **8 Cost / COGS** | One configuration decision with five consequences (`P11-C-13`); conversion cost zero; 30 records ±1.5 × 10²¹ |
| **9 AR / AP / cash / bank** | ~~Arithmetic sound **at a declared tolerance** (`F-02`)~~ **SUPERSEDED `2026-09-08` (`P11-C6-01`, `RC06-F1`).** **Arithmetic sound at EXACT EQUALITY and at every tested tolerance** — `0` unbalanced posted entries at exact equality, `1e-7`, `1e-4` and `0.005`, on both the computed debit−credit and the stored balance column, across the **four frozen RC-05 database extracts** (`DB-SM` 169,143 · `DB-BK` 16 · `DB-EV` 6 · `DB-T2` 5 posted entries with lines). Owner evidence: **P08 `f0cf287ac9f4ad37b0c19145df4a0e396af84c13`**. **The old wording was the practical residue of the very rule this file withdraws** at §-`F-02`: *"a soundness claim without a tolerance is not a claim."* **Restated without re-grounding it** — this instance supports no requirement that soundness be stated only at a declared tolerance, because here there is no tolerance at which the count is non-zero. **P11 does not re-derive P08 balances**; it consumes them. **Four frozen extracts are NOT an established deployment census**, and P11 preserves that uncertainty rather than upgrading it. | **10 of 1,904** payables invisible to a type-scoped ageing |
| **10 Analytic** | `OC-08` gross-not-net, **43×** — **unchanged by CORR3 and still P11's strongest own statement** |
| **11 Tax / localisation** | `P08-HO-14` new from `P08`: the statutory register family selects on **two different period bases**, so **5,228 entries** can appear in one register and not the other. **No statutory determination made** |
| **12 Correction / reversal** | **The invariant fails here** (`P11-C-15`) — and `P08-HO-13`'s deletion path **bypasses correction entirely** |
| **13 Period / cut-off** | `T0-15` **re-scoped to 18.0** (`F-04`) |
| **14 Scope** | Unchanged; `P02` independently requires **deny-on-missing-scope** |
| **15 Duplicate / orphan / unowned** | `P08-HO-13` adds a **new duplicate mechanism**: an entry-number **sequence reset to 1 permits previously-issued numbers to be re-issued** |
| **16 Candidate I/P/O/H** | Re-derived in `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` |

### 2.1 Same economic event under two terminologies — the §10 test

| Apparently two | Evidence they are one | Disposition |
|---|---|---|
| `P02`'s *"invariant fails at correction/reversal"* and `P10`'s recognition-side conclusion | Same invariant, same named failure point, **independent evidence** | **ONE finding, two witnesses** — `P11-C-15`. **Not double-counted** |
| `P01`'s `om_data_remove`, `P06`'s v19 module, `P08`'s `P08-HO-13` | Same mechanism class, **three different database populations** | **ONE mechanism, three scopes.** Counted once; scopes listed separately |
| `P01`'s `฿29.0m` received-not-invoiced and `P08`'s completeness gap | `P01` routes it **to** `P08` | **ONE question, one owner (`P08`), one decision (Boss).** Not two items |

**3 candidate double-counts tested, 3 collapsed to single findings.**

**`CP-P11C3-05`/`-06` — COMPLETE — EVIDENCE VERIFIED.**
