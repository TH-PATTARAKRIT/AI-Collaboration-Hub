# P08_AAS03_TARGETED_CHALLENGE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T14`

Four AAS-03 experts challenged the targeted closure independently and concurrently, none seeing another's work. Two carried a mandated disproof target.

| Expert | Discipline | Mandated to disprove |
|---|---|---|
| **E1** | Leader Functional Design | **"The journal item is the accounting source of truth."** |
| **E2** | Leadership Database Design | — re-run all 11 published measurements, then attack the data on its own initiative |
| **E3** | Lead Integration & Localization | — the version boundary, deployment gating, statutory register, peer attribution |
| **E4** | Lead Code & UI Architect / method | **"No independent Accounting Event identity exists."** — plus `MC-01..10`, `EC-01..08` |

**Verification rule applied to every reviewer claim before adoption:** *Independent Review ≠ Truth. Verified Evidence = Truth Basis.* The author re-ran each material finding against the primary evidence. **Two reviewer claims failed that check and are recorded as such in §5.**

---

## 1. Convergence — the strongest signal in this round

**Three of the four experts independently found the same defect, by three different routes, without contact:** the orphan-entry population omitted the two origin pointers populated at scale.

| Expert | Route | Figure reached |
|---|---|---|
| **E1** | noticed file 38 contradicted file 41's own class table | 9,754 |
| **E2** | derived the origin-carrier set from the table schema rather than accepting the author's | 9,754, refined to **6,585** |
| **E4** | audited the denominator discipline and found the column set author-chosen | 9,754 |

**The author verified all three and E2's refinement.** The published figure was **83,820**. The defensible figure is **6,585 — 3.9% of posted entries** once the 3,169 entries reachable as a settlement's exchange entry are also removed. **Over-claim factor 12.7×.**

`47` §1 published the intermediate 9,754 and is superseded here. **One further correction to `47` §1:** the 5,786 no-reference count attaches to the 9,754 tier; at the 6,585 tier it is **2,617**.

**A defect three independent reviewers find on first contact, that three of the author's own revalidation phases did not, is not an unlucky slip. It is the author's method failing at a specific point: choosing a predicate instead of deriving it.**

## 2. The two mandated disproofs

### 2.1 "The journal item is the accounting source of truth" — **CONTRADICTED AS AN ABSOLUTE**

E1 did not disprove it outright and does not recommend the converse. It disproved it **for six of the eight properties that make a record an accounting record.** The author verified the load-bearing half of the argument directly: the balance invariant is computed by grouping items **by entry**; the seal, the sequence counter, the reversal link and the posting state are entry-level columns absent from the item table.

| Dimension | Source of truth |
|---|---|
| Measurement — amount, currency | **Item** |
| Account attribution | **Item** |
| Party attribution | Item together with the settlement graph |
| Recognition date, period attribution | **Entry** |
| Finality and posting state | **Entry** |
| Number and sequence identity | **Entry** — and unrecoverable from **41.9%** of posted items |
| Immutability and correction lineage | **Entry** |
| Provenance | **Entry** for the majority of posted items |

**Adopted.** The atomic unit is **the entry together with its item set**. `45` §2 and `47` §8 carry the corrected answer.

E1 further showed the package concedes at least **four competing truth bearers** in its own published findings — report-layer stores holding figures not derived from items, the fixed-asset register and inventory valuation record as genuine separate stores with no reconciliation obligation, and the report definition itself. **Any one of these falsifies the unqualified claim.** Accepted.

### 2.2 "No independent Accounting Event identity exists" — the disproof **partly succeeded against the author, in the author's favour and then against it**

This claim had **already been withdrawn** by the author in `39`. E4 tested the withdrawal itself and found the author's evidence for it **partly false**.

**`P08-CONTRA-32` — a counterexample published as "read directly" does not hold.**

The author published: *"a payment transaction carries a database `UNIQUE` constraint on the provider's reference."* **Verified by the author against source: false.** The constraint sits on the transaction's **own internally generated reference** — documented in the source as *the internal reference* and computed by the system from a prefix and a sequence number. The **provider's** reference carries **no constraint at all**.

By the author's own argument three paragraphs later — that a uniqueness index on a system-generated number is *"structurally incapable of colliding"* and therefore not event identity — **this counterexample proves the opposite of what it was cited for.**

| The four counterexamples, re-assessed | Standing |
|---|---|
| Bank statement line — import key under a uniqueness constraint | **VERIFIED** by the author and independently by two reviewers |
| Bank statement line delegated 1:1 to the entry | **VERIFIED**, but E1 is right that a 1:1 delegate is **not** an event object: it shares the entry's lifecycle and is cascade-deleted with it. It expresses neither one-to-many nor many-to-one |
| Payment transaction reference | **STRUCK — `P08-CONTRA-32`** |
| Electronic-invoicing constraint | **NOT INDEPENDENTLY READ** by the author; and E3 established the module is **uninstalled in both 19.0 databases** |

**The withdrawal of the class-A claim stands** — it rests on the bank-statement evidence, which three parties verified. **But the corrected finding over-stated its base and is narrowed here:**

> Durable event identity exists as an **import de-duplication key on one inbound channel**, enforced by a uniqueness constraint on a **nullable** column, **unpopulated on all 13,814 deployed rows**. It is not an accounting-event object: nothing in the searched scope carries identity **independent of the journal entry**.

**And E1's third point is adopted:** withdrawing the absolute left **no successor claim**. The correctly-scoped negative — *no accounting-event object with identity independent of the journal entry exists* — **remains untested across the root set.** The register row is **re-opened, not closed by re-classification.**

## 3. Corrections against the author, verified — beyond those in `47`

| ID | Finding | Author verification |
|---|---|---|
| `P08-CONTRA-32` | The payment-transaction counterexample is false | **CONFIRMED** against source. §2.2 |
| `P08-CONTRA-33` | **A withdrawn class-A claim is still carried at class A** — in the promotion summary, and as *"the finding that governs this whole register"* opening the accounting-event register — while the negative-claim register certifies *"none found"* | **CONFIRMED in 2 of the 3 places named.** The reviewer also claimed the claim's own row was unchanged; **it is not — it is correctly struck through and marked withdrawn.** Recorded in §5 |
| `P08-CONTRA-34` | **"N of 21 roots" is at most 7 independent observations** | **CONFIRMED by content hash.** 22 roots; 20 carry the core posting file; **7 distinct contents**. Every root-set negative overstates its support by roughly threefold |
| `P08-CONTRA-35` | *"In a real population the duplicate detector is swamped"* is unsupported by the author's own data | **CONFIRMED.** Scoped to the population the detector covers: **677 of 36,961 in 289 groups, largest 14** — not swamping. **32,227 of the published 33,147 (97.2%) sit in the class the detector never inspects** |
| `P08-CONTRA-36` | **The 19.0 ledger account is not company-owned and has no code column** — the account-identity model describes only the 16.0 shape | **CONFIRMED.** 16.0 carries both columns; **both 19.0 databases carry neither.** `40` caught the version boundary on two minor columns and missed it on the most load-bearing table in the package |
| `P08-CONTRA-37` | **No register was updated by the closure** | **CONFIRMED.** **0 of 8** closure identifiers tested appear in any pre-closure register. Corrected in this round — see the closure deltas appended to `17`, `27`, `28`, `29` |
| `P08-CONTRA-38` | The custom-module denominator of 30 is not reproducible from the criteria as stated; one criterion is prose, not a pattern | **ACCEPTED.** Two reviewers derived 28 independently. The author does not re-assert 30 |
| `P08-CONTRA-39` | File 34 publishes **neither the command nor its output** for any of the 14 re-runs — the standing rule is to publish both | **ACCEPTED. File 34 is not reproducible as written.** This is why two of its controls were only caught by reviewers building their own patterns |
| `P08-CONTRA-40` | The zero-drift result depends on an undeclared tolerance: at exact zero, **2,354 of 100,580** lines differ by 1e-11 to 1e-13 because the settlement amount is a floating-point column | **ACCEPTED.** The conclusion holds at any tolerance ≥ 1e-6; the tolerance must be published with it |

## 4. Findings where the package **understated** — verified additions

**The evidence base was read once and not exhausted.** Four of these settle claims the author was holding at `HOLD — RUNTIME EVIDENCE REQUIRED` **using data the session already had.**

| ID | Finding | Author verification |
|---|---|---|
| `P08-F-41` | **30 posted entries carry a Buddhist-Era accounting date.** Year 2567, one journal, created 2024. **The entry numbers embed the bad year**, so the numbering is permanently wrong. These entries fall in no fiscal year any report covers | **CONFIRMED exactly** — 30 entries, 120 items. This is the **live instance** of the package's theorised system-derived, unvalidated accounting date, and it is the source of the extreme the author rounded away |
| `P08-F-42` | **Positive residue of deleted posted entries.** 18 journal items carry a stored entry number naming an entry **that exists nowhere in the entry table**; each now belongs to a different, cancelled entry on the same date | **CONFIRMED exactly** — 5 distinct absent numbers, 18 items; control passes on a known-present number. **This settles `AT-15` and `JPM-16`**, both of which the author held as untestable in a snapshot on the grounds that *"a deleted entry leaves no row to count"* and *"a historical mutation leaves no trace."* **The denormalised parent number is that trace.** `P08-M-14` |
| `P08-F-43` | **The settlement chronology defect points both ways.** The author published only the late side; **28,229 of 63,773 settlements (44.3%) were created *before* their own as-of date**, worst case 335 days early | **ACCEPTED** — a population nearly as large as the published one, omitted |
| `P08-F-44` | The future-dated extreme is **198,326 days** — 543 years — and is suppressed by publishing only the backdated maximum beside the future-dated count | **ACCEPTED.** Caused by `P08-F-41` |
| `P08-F-45` | **A posted entry is booked in another company's journal** — deployed data, 19.0 | **CONFIRMED.** 1 of 16 posted entries in that database. The author asserted this class **from source and never tested it** |
| `P08-F-46` | **38 posted entries have every line zero in both frames** — posted entries with no financial effect. Posted entries with **no lines**: 0 | **CONFIRMED.** The reviewer counted 36; the author counts 38 on its own zero test. The attack's realised form here is the **zero-value** entry, not the zero-line entry |
| `P08-F-47` | The four genuine transaction-currency imbalances share one mechanism: an **implied rate of exactly 1.000**. Across all 34,135 foreign posted items, **exactly 4 carry that rate, and they are these** | **ACCEPTED.** The root cause is the **1:1 rate fallback**, not the currency frame of the balance assertion. `43` §6's argument is re-grounded |
| `P08-F-48` | **32 modules installed in a deployed database exist in neither searched source tree** — including two touching ledger numbering, one writing the rate master on which a class-A absence rests, and one able to carry arbitrary models and server-side automation — **the residual route `44` §5 left open** | **ACCEPTED, GATING.** Raised independently by E3 and E4. Re-classified from `C NOT YET SEARCHED` to a **gating** unknown: the constitution forbids carrying a current-scope blocker as an unsearched class. `P08-U-18` |
| `P08-F-49` | A **statutory register query with no company predicate**, installed on two 44-company databases, sits in the package's own quarantine and reached no Layer-1 file | **ACCEPTED.** `P08-U-19` |
| `P08-F-50` | **Two disjoint statutory reporting stacks** exist across the estate; the sweep examined one and generalised | **ACCEPTED.** `P08-U-20` |

## 5. Where the reviewers were wrong — verified, and recorded

**Reviewer findings are not automatically true, and two did not survive.**

| Reviewer claim | Author verification |
|---|---|
| **E4:** the withdrawn class-A claim's own row in the root-set declaration is *"unchanged"* at class A | **FALSE.** The row **is** struck through and marked `WITHDRAWN — CONTRADICTED`. The reviewer's finding is right about **2 of the 3** locations and wrong about the one it leads with. `P08-CONTRA-33` is adopted at its correct scope |
| **E2:** the no-reference count of 5,786 *"stands unchanged"* at the corrected orphan population | **IMPRECISE.** 5,786 is correct at the **9,754** tier; at the reviewer's own **6,585** tier it is **2,617**. Verified by the author |
| **E4:** 21 roots carry the core posting file | **21 vs 20** on the author's re-derivation. **Immaterial** — the finding is the number of *distinct contents*, which both parties measure as **7** |

**This is the fourth time this programme has recorded that independent review commits bounded-enumeration errors of its own.** It does not weaken the three verified corrections above it; it is why every one of them was re-run before adoption.

## 6. Vetoes

Four experts, four vetoes, all scoped rather than blanket. **None vetoes the session; each vetoes reliance on specific artefacts.**

| Veto | Scope | Lifting conditions |
|---|---|---|
| `AAS03-E1-VETO-01` | `KRN-INV-00` and any artefact inheriting *"sum to zero in every currency frame"*; and the headline wording of the orphan, imbalance and backdating findings | 5 conditions — the invariant split per `P08-BD-18`, and the three findings restated. **4 of 5 discharged** in `47`; the invariant split is **`HOLD — AUTHORITATIVE ACCOUNTING-STANDARD EVIDENCE REQUIRED`** and is not the author's to settle |
| `AAS03-E2-V-01` | Reliance on the 83,820 orphan figure, the 53 imbalance figure, and the "0 of 64 journals" denominator | 4 conditions. **3 discharged** in `47` and §1 here. The fourth — **republish every measurement with its predicate in executable form beside its result** — is **NOT DISCHARGED** and is carried to the handoff |
| `AAS03-E3-VETO` | The closure's **deployment-status and localization conclusions** — specifically *"the most severe code findings are largely not deployed"* | 5 conditions. **2 discharged** (`47` §4, §7). Three remain, all turning on `P08-U-18` |
| `AAS03-E4-V-01` | Reliance on **files 34, 38 and 39 §1** — explicitly not on the session | 5 conditions. **2 discharged.** Conditions on file 34's reproducibility and on the 32 unexamined modules remain |

**Four independent vetoes converge on one lifting condition the author cannot discharge from this host: `P08-U-18`.**

## 7. Convergence and exit assessment

The author accepts E4's method assessment rather than contesting it, with two corrections of scope.

| | E4 verdict | Author disposition |
|---|---|---|
| `MC-01` Population boundedness | NOT MET | **ACCEPTED** — `P08-U-18` is gating and was mis-filed |
| `MC-02` Systematic enumeration | NOT MET | **ACCEPTED** — `P08-CONTRA-39` |
| `MC-03` Independent delta test | NOT MET | **ACCEPTED** — this pass returned three new material classes |
| `MC-04` Repeatability | PARTIAL | **ACCEPTED.** The root set and every database measurement reproduce exactly; file 34 does not |
| `MC-05` Negative-claim compliance | NOT MET | **ACCEPTED** — `P08-CONTRA-33`, `-34` |
| `MC-06` Unknown classification | NOT MET | **ACCEPTED at the time of the finding; PARTIALLY REMEDIED** by this round's register deltas |
| `MC-07` Contradiction closure | NOT MET | **ACCEPTED at the time; PARTIALLY REMEDIED**. The 38↔41 contradiction is now resolved and recorded |
| `MC-08` Tolerance-zero closure | NOT MET | **ACCEPTED.** 0 boundaries closed; two moved the wrong way |
| `MC-09` Evidence lineage | NOT MET | **ACCEPTED at the time; PARTIALLY REMEDIED** |
| `MC-10` New-finding delta threshold | NOT MET | **ACCEPTED** — every one of E1's, E2's and E4's headline findings is gate-changing |

**CONVERGENCE: NOT ACHIEVED.**

**`EC-01` … `EC-08`: 0 of 8 met.** The author accepts E4's assessment in full. `EC-07` — two consecutive clean independent passes — is the decisive one and is furthest from being met: **this pass was not clean, and it found an evidence-integrity failure inside the author's own previous correction.**

## 8. What this round actually established

**The measurement layer is sound and the interpretation layer is not.** Across four independent reviewers, **every figure the author published reproduced to the digit** — the root set, 447,384 items, 169,143 posted, 0 unbalanced, 63,773 settlements, 13,814 statement lines, 0 seals, 0 locks, every gating row of the module sweep. Not one arithmetic error was found.

**Every material defect was a wrong predicate, not a wrong calculation:** a link set that omitted two populated columns; an invariant applied to entries it does not govern; a denominator summed over two databases instead of three; a control that proved a pattern produced output rather than that it matched the claim; a counterexample read for the wrong column.

> **`P08-M-15` — arithmetic discipline does not protect against predicate error, and a positive control that tests the instrument does not test the claim. This programme has now recorded that lesson five times in one session and breached it four times in the same session.**

**Author's own record on this round: 0 of the 19 corrections in `47` and §3 were self-caught.** Three self-review phases preceded four expert challenges; the challenges found every one. That ratio — recorded for the fifth time in this programme — is the strongest single argument in the package for the standing rule that **no P08 conclusion may reach the Boss without an independent pass that is free to attack it.**
