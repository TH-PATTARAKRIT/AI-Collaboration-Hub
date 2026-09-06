# P11 — CORR3 RE-CONVERGENCE AND FALSIFICATION PASS

`[SMEPLUS-26-09-06-…-CORR3-ACCOUNTING-INTAKE-INTEGRITY-001]` · `CP-P11C3-05`/`-06` · **PHASE S** · AI EOS **OFF**

> Run **only after** intake integrity was established (`P11_CORR3_INTAKE_INTEGRITY_AND_DENOMINATOR.md`).
> **§11 discipline: for every load-bearing claim, P11 attempts to DISPROVE it before carrying it.**

---

## 1. Falsification pass

| # | Claim | Supporting evidence | Counterexample sought | Counterexample **found** | Resolution | Residual risk |
|---|---|---|---|---|---|---|
| `F-01` | **The settlement graph is reconcilable** (`CI-02`, from `P08` §1 item 2) | 63,773 records / 100,580 lines, residual drift 0 | a mechanism that removes settlement rows outside the object layer | **YES — `P08-CONTRA-55`/`HO-13`.** A module **installed in all three deployed databases** deletes the settlement table, then journal items, then entries, in unqualified raw SQL, **committing per table**, and **resets the entry-number sequence to 1** | **Claim WITHDRAWN.** P08 withdraws it against its own package | Whether it has executed is **unverified by P08**; a peer observation is carried **attributed, not re-derived** |
| `F-02` | **The ledger is arithmetically sound — 0 unbalanced across 169,143** | `P08` §1 item 1 | a tolerance at which the count is non-zero | **YES.** 0 holds **at tolerance ≥ 0.005**; **at 1e-7 the answer is 3** — float artefacts on eight-figure sums. And **the word "complete" is WITHDRAWN** (`P08-CONTRA-73`) | **Re-stated with its tolerance.** *Arithmetically sound at a declared tolerance* — never *complete* | A soundness claim without a tolerance is not a claim |
| `F-03` | **96.1 % of posted entries carry an origin pointer** | `P08` §1 item 5 (CORR2) | a stricter predicate for *origin pointer* | **YES — `P08-CONTRA-63`.** **78.03 %** carry a **structured** pointer; 96.1 % counted **free-text reference**. **~30,750 entries' only provenance is unparsed text** | **Corrected to 78.03 %** | P08 records the figure moved **12.7× down then 5.6× up** across two rounds, *"both from predicate error"* |
| `F-04` | **There is no accounting period to reconcile within** (`T0-15`) | `P08` `A VERIFIED ABSENCE`; 0 of 6 companies close; no lock date on 3 surfaces | a period-like object in **another generation** | **YES — `P08-CONTRA-68`.** Absent **in the declared 18.0 root set only**. *"The 19.0 line carries a dated, recurring return object, and both 19.0 deployed databases carry its linking column on the entry table"* | **`T0-15` RE-SCOPED to the 18.0 source line.** P08's instruction quoted: ***"P11 must not receive the absolute"*** | A tax return is not a general accounting period; the 19.0 object's accounting sufficiency is untested |
| `F-05` | **Settlement chronology is untrustworthy — 46.4 % after / 44.3 % before as-of date** (`CQ-P11-04`) | `P08` §2 item 5 (CORR2) | that the two dates are not comparable | **YES — `P08-CONTRA-57`.** The as-of date is **computed by the kernel** as the later of the two items' accounting dates; the split compared a **write timestamp** against a **derived date** and *"**contains no defect**"* | **WITHDRAWN.** P11 carried a non-defect as a finding for one round | `CQ-P11-04`'s *"four distinct times"* loses its strongest support |
| `F-06` | **`฿29,029,467.66` is the largest unrecognised accounting position** (`B-28`, CORR2) | `P01` §6 | the owner's own classification | **YES.** *"**This is a timing position, not a missing transaction** … under periodic valuation no receipt-time entry is expected … **P08's judgement and the Boss's decision**"* | **Framing WITHDRAWN.** Carried as `CANDIDATE INPUT — NOT PROMOTED`. **`฿1,538,601.86` of it is operator-typed with no receipt document and must not be read as received** | The completeness question at a reporting date is real and is **not P11's to answer** |
| `F-07` | **`P11-C-12` — reconciliation exists where vacuous, absent where meaningful** | `P08` kernel; P11's `0 of 7 unqualified` | a case where the party-dimension identity fails | **YES, twice.** `P01`: **10 of 1,904** vendor bills balance to a non-payable account — *"a payables ageing scoped to the payable account type **will not see these liabilities**"*. And **`P08-U-28`**: *"every kernel claim in this handoff rests on the 18.0 line. **No deployed database runs it**"* | **Downgraded to `SUPPORTED INTERPRETATION — 18.0 SOURCE LINE`** and carried under `AAS+-VETO-01` | The claim may not be true of **any** deployed generation. It was P11's headline for one round |
| `F-08` | **`P11-C-15` — the governing invariant fails at correction/reversal** | `P02` `43_` §5; `P10` reached it from the recognition side | that one relayed it from the other | **NO.** Different packages, different evidence, **neither cites the other**, and the failure point is named identically | **CARRIED as a convergence** — the first with a *tested* independence claim | Both are 18.0-line statements |
| `F-09` | **`B-21`/`T0-14` — deletion path installed** | `P01` series-16 `16.0.1.0.1` + FK; `P06` v19 non-target | that it is confined to one non-target database | **NO — it is WIDER.** `P08` `HO-13`: **installed in all three deployed databases** | **STRENGTHENED, scope corrected: three deployed databases across two generations** | `installed` ≠ `exercised`. P09's five-rung ladder applies: **exercised NOT ESTABLISHED** |
| `F-10` | **`B-26` — the deletion explanation covers the valuation-layer zeros** | `ON DELETE SET NULL` + installed module | a zero the mechanism cannot produce | **Already found at CORR2** (3 of 6 incoherent). **Sought again against `HO-13`'s wider table set** — settlement, items, entries | **Bounded held**, and **widened to the settlement graph** (`F-01`) | The universal stays withdrawn |

**10 claims tested. 8 counterexamples found. 5 claims withdrawn or re-scoped. 1 strengthened. 1 survived.**

> ### `P11-F-16` — **the falsification pass disproved more of P11's own carried claims than the four-expert challenge did.**
> Every one of `F-01` … `F-06` was disproved **by the owner's own current statement**, sitting in the
> frozen snapshot, requiring no new research — only reading the artefact at the head P11 had already
> resolved. **Attempting disproof first is cheaper than being corrected, and it found more.**

---

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
| **9 AR / AP / cash / bank** | Arithmetic sound **at a declared tolerance** (`F-02`); **10 of 1,904** payables invisible to a type-scoped ageing |
| **10 Analytic** | `OC-08` gross-not-net, **43×** — **unchanged by CORR3 and still P11's strongest own statement** |
| **11 Tax / localisation** | `HO-14` new from `P08`: the statutory register family selects on **two different period bases**, so **5,228 entries** can appear in one register and not the other. **No statutory determination made** |
| **12 Correction / reversal** | **The invariant fails here** (`P11-C-15`) — and `HO-13`'s deletion path **bypasses correction entirely** |
| **13 Period / cut-off** | `T0-15` **re-scoped to 18.0** (`F-04`) |
| **14 Scope** | Unchanged; `P02` independently requires **deny-on-missing-scope** |
| **15 Duplicate / orphan / unowned** | `HO-13` adds a **new duplicate mechanism**: an entry-number **sequence reset to 1 permits previously-issued numbers to be re-issued** |
| **16 Candidate I/P/O/H** | Re-derived in `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` |

### 2.1 Same economic event under two terminologies — the §10 test

| Apparently two | Evidence they are one | Disposition |
|---|---|---|
| `P02`'s *"invariant fails at correction/reversal"* and `P10`'s recognition-side conclusion | Same invariant, same named failure point, **independent evidence** | **ONE finding, two witnesses** — `P11-C-15`. **Not double-counted** |
| `P01`'s `om_data_remove`, `P06`'s v19 module, `P08`'s `HO-13` | Same mechanism class, **three different database populations** | **ONE mechanism, three scopes.** Counted once; scopes listed separately |
| `P01`'s `฿29.0m` received-not-invoiced and `P08`'s completeness gap | `P01` routes it **to** `P08` | **ONE question, one owner (`P08`), one decision (Boss).** Not two items |

**3 candidate double-counts tested, 3 collapsed to single findings.**

**`CP-P11C3-05`/`-06` — COMPLETE — EVIDENCE VERIFIED.**
