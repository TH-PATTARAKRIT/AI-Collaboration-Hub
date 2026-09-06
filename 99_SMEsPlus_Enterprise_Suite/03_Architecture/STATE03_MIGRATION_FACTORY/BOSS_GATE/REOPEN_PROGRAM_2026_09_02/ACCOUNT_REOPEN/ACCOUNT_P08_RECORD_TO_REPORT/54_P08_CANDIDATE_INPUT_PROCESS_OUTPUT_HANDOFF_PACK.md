# P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S CANDIDATE — NOT A CONTRACT**

**Nothing here is a final cross-domain contract.** Every cross-domain item is a **CANDIDATE** awaiting **PHASE B** Producer/Consumer validation under AI EOS, which is **OFF** in Phase S.

**Reading rule.** *Evidence Class* is the class of the **ledger-boundary fact**, never of the producing domain's internals. Where a producer is named it is named as a **candidate counterparty**, not as researched fact.

**Scope key:** `PLAT` platform · `TEN` tenant · `CO` company. **Version key:** `S18` 18.0 source · `D16` `DB-SM` · `D19` `DB-BK`/`DB-EV`.

---

## 1. CANDIDATE INPUT — what presents itself at the ledger boundary

| ID | Type | Business Meaning | Evidence Class | Source Candidate | Scope | State/Timing | Correction/Reversal | Evidence Ref | Open Dependency |
|---|---|---|---|---|---|---|---|---|---|
| `IN-01` | CANDIDATE INPUT | An accounting assertion with no document behind it — the plain journal entry | `FACT VERIFIED — P08` (D16: 129,577 posted, 92.5% carry a pointer) | P08 itself, or any process | `CO` | proposed at create; effective at post | reversible by entry-level link | `53` CQ-01, `41` | none |
| `IN-02` | CANDIDATE INPUT | The ledger effect of a purchase-side document | `FACT VERIFIED — P08` (D16: 36,867 posted; **internal producer link 26.8%**, **external document reference a further 72.6%**, party 100%) | P01 / P05 | `CO` | document date proposed; **accounting date system-derived** | reversible; cancellation destroys settlements | `53` CQ-01, CQ-04 | **CORRECTED `P08-CONTRA-48`** — the previous "producer identity absent on 73.2%" rested on an undeclared pointer-only predicate |
| `IN-03` | CANDIDATE INPUT | The ledger effect of a sale-side document | `FACT VERIFIED — P08` (D16: 2,599 posted, 84.1%) | P02 | `CO` | **exempt from date derivation** | as above | `53` CQ-01 | none |
| `IN-04` | CANDIDATE INPUT | A credit/refund ledger effect | `FACT VERIFIED — P08` (D16: 100 posted, 93.6–100%) | P01, P02 | `CO` | as its parent class | as above | `53` CQ-01 | none |
| `IN-05` | CANDIDATE INPUT | A settlement instruction pairing two ledger items | `FACT VERIFIED — P08` (D16: 63,773 records, 100,580 lines) | P06 | `CO` | **CORRECTED `P08-CONTRA-57`: the as-of date is NOT producer-supplied — it is computed by the accounting kernel as the later of the two items' own accounting dates.** P08 controls it | settlement is destroyed by cancelling either side | `53` CQ-09, `58` | **The 46.4%/44.3% split compared a system write timestamp against a derived accounting date and evidences no defect. WITHDRAWN** |
| `IN-06` | CANDIDATE INPUT | An asset lifecycle ledger effect | `FACT VERIFIED — P08` (D16: 17,513 posted entries carry an asset pointer) | P04 | `CO` | commonly **bulk-generated**; 6,306 arrived in a single catch-up | reversible | `47` §3, `48` §4 | **a separate register exists with no reconciliation obligation** |
| `IN-07` | CANDIDATE INPUT | An inventory valuation ledger effect | `FACT VERIFIED — P08` (D16: 56,589 posted entries carry a valuation pointer) | P03 / inventory | `CO` | at valuation event | reversible | `48` §1 | **separate store, no reconciliation obligation** |
| `IN-08` | CANDIDATE INPUT | A **tax-period stamp** arriving on the entry, distinct from the accounting date | `FACT VERIFIED — P08` (D16: **61,157 posted entries**, 5,228 differ from the accounting date, 1,316 by month) | P07 | `CO` | stamped at create | **the two carriers disagree on 4,393 items (24.2%), 747 by month** | `49` §3, `53` CQ-08 | **CORRECTED `P08-CONTRA-58` — see the decomposition below.** Carrier present in one 19.0 database at **0** population and absent in the other; a **second** carrier exists in both 19.0 databases and is unexamined |
| `IN-09` | CANDIDATE INPUT | A currency rate applied to a foreign leg | `FACT VERIFIED — P08` | **CORRECTED `P08-CONTRA-59`: not a "platform rate master" — an external third-party HTTPS endpoint on a daily scheduled job, live in `DB-SM`** | `PLAT`→`CO` | at post; **rate may be silently stale, and a failed fetch is a logged warning only** | — | `43`, `49` §4 | **A 1:1 fallback is reachable, but "all 4 imbalances come from it" is FALSE — one is a rounding residue at rate 35.39** |
| `IN-10` | CANDIDATE INPUT | Company and journal assignment | `FACT VERIFIED — P08` | the calling context | `CO` | at create | not re-validated at post | `53` CQ-10 | **a posted entry exists in another company's journal** (D19) |
| `IN-11` | CANDIDATE INPUT | A caller-supplied control key altering ledger validation | `FACT VERIFIED — P08` (S18: 134 keys, **47 behaviour-altering**, 2 secure by default) | any caller | `PLAT` | per call | — | `44` | **the balance invariant is one of the 47** |

**`IN-02`, `IN-05`, `IN-06`, `IN-07`, `IN-08` name a candidate producer. P08 has NOT researched any producer's lifecycle and does not assert how any of them decided to emit the event.**

---

## 2. PROCESS — what the ledger actually does

| ID | Type | Business Meaning | Evidence Class | Scope | State/Timing | Correction/Reversal | Evidence Ref | Open Dependency |
|---|---|---|---|---|---|---|---|---|
| `PR-01` | PROCESS | Accept an entry and validate its structure | `FACT VERIFIED — P08` | `CO` | at create and at post | — | `43` | — |
| `PR-02` | PROCESS | **Derive the accounting date** — for non-sale documents, from the clock and the document date, **with no lock involved** | `FACT VERIFIED — P08` (S18 mechanism; D16 shows 20.95% vs 0.12% divergence) | `CO` | at create and on any document-date change | silent; **no attributable trace** | `46` §6 | backward divergences `UNRESOLVED` |
| `PR-03` | PROCESS | **Assert double entry in the reporting currency** | `FACT VERIFIED — P08` — **one line of defence, object layer, disabled by a caller-supplied value** | `CO` | at post | — | `43` | `KRN-INV-00` **CONTESTED**, `P08-BD-18` |
| `PR-04` | PROCESS | Assign the entry number | `FACT VERIFIED — P08` | `CO` | **at post** | number is retained through cancellation | `53` CQ-03, `49` §2 | **deployed numbering ≠ source numbering**; collision-freedom `UNRESOLVED` |
| `PR-05` | PROCESS | Transition draft → posted | `FACT VERIFIED — P08` | `CO` | at post | reversible to draft by cancellation | `53` CQ-03 | **state is outside the seal's field set** |
| `PR-06` | PROCESS | Seal the entry against alteration | `FACT VERIFIED — P08` — **optional, and off on 0 of 29 transacting journals** | `CO` | at post, if enabled | — | `53` CQ-03, CQ-10 | — |
| `PR-07` | PROCESS | Maintain settlement pairs and residuals | `FACT VERIFIED — P08` — **residual drift 0** at tolerance ≥ 1e-6 | `CO` | on settle/unsettle | destroyed by cancelling either side | `53` CQ-09 | **tolerance must be published with the result** |
| `PR-08` | PROCESS | Reverse, cancel or supersede | `FACT VERIFIED — P08` | `CO` | any time; **no lock guard inside either settlement model** | **lineage is entry-level only and is destroyed by cancellation** | `53` CQ-06 | 5 entries deleted with items surviving |
| `PR-09` | PROCESS | Evaluate a period lock | `FACT VERIFIED — P08` — **relocates rather than refuses** | `CO`, inherited across the hierarchy | at post | the relocation itself is the correction | `36`, `53` CQ-04 | `P08-BD-16` |
| `PR-10` | PROCESS | Propagate company scope onto items | `FACT VERIFIED — P08` — mirrors agree on 447,384 of 447,384 | `CO` | at create | — | `41` §2 | **the entry-number mirror does NOT agree — 174,977 disagree** |

---

## 3. CANDIDATE OUTPUT — what P08 can offer a consumer

| ID | Type | Business Meaning | Evidence Class | Consumer Candidate | Scope | State/Timing | Correction/Reversal | Evidence Ref | Open Dependency |
|---|---|---|---|---|---|---|---|---|---|
| `OU-01` | CANDIDATE OUTPUT | A posted, numbered journal entry | `FACT VERIFIED — P08` | all | `CO` | at post | reversible | `53` CQ-03 | **The number is NOT an entry identifier** — 4,722 numbers are each held by two posted entries (`P08-CONTRA-62`). Unique within a journal only. And the entry is **not immutable** beyond the nine default-guarded fields |
| `OU-02` | CANDIDATE OUTPUT | The journal item set — the monetary decomposition | `FACT VERIFIED — P08` | all, and every report | `CO` | at post | — | `41` | **41.89% cannot name their entry** |
| `OU-03` | CANDIDATE OUTPUT | General ledger | `FACT VERIFIED — P08` — **derived at read time, no stored ledger** | P11, reporting | `CO` | on demand | reflects current state only | `53` CQ-08 | **no as-of reconstruction** |
| `OU-04` | CANDIDATE OUTPUT | Trial balance | `FACT VERIFIED — P08` — **derived, no stored TB** | P11, reporting | `CO` | on demand | as above | `53` CQ-08 | balances **only** in the enforced frame |
| `OU-05` | CANDIDATE OUTPUT | Balance sheet and profit-and-loss | `FACT VERIFIED — P08` | Boss, statutory | `CO` | on demand | as above | `45` hop 9 | **reads no provenance**; three side-stores hold non-ledger figures |
| `OU-06` | CANDIDATE OUTPUT | Settlement and residual state | `FACT VERIFIED — P08` | P06, P11 | `CO` | current only | destroyed by cancellation | `53` CQ-09 | **no bitemporal record** |
| `OU-07` | CANDIDATE OUTPUT | Party ageing | `SUPPORTED INTERPRETATION — P08` | P01, P02, P11 | `CO` | current only | — | `53` CQ-09 | **a re-run prior-period ageing is not the report that was run then** |
| `OU-08` | CANDIDATE OUTPUT | A statutory register feed | `FACT VERIFIED — P08` | P07 | `CO` | on demand | — | `42`, `49` §3 | **tax period absent at item level; one register query has no company predicate** |
| `OU-09` | CANDIDATE OUTPUT | The year-end result | `FACT VERIFIED — P08` — **derived at report time; no posted closing entry exists** | Boss, statutory | `CO` | on demand | — | `53` CQ-04 | `P08-BD-06` |

---

## 4. CANDIDATE HANDOFF — leaving P08

| ID | Type | Business Meaning | Evidence Class | Consumer Candidate | Scope | Must wait for PHASE B? | Evidence Ref |
|---|---|---|---|---|---|---|---|
| `HO-01` | CANDIDATE HANDOFF | The ledger contract every process must satisfy to post | `CANDIDATE HANDOFF` | **P11** | `PLAT` | **YES** | `58` |
| `HO-02` | CANDIDATE HANDOFF | What P11 must reconcile, and what the ledger cannot supply for it | `CANDIDATE HANDOFF` | **P11** | **YES** | `58` |
| `HO-03` | CANDIDATE HANDOFF | **Correction to a prior P08 answer:** a tax-period carrier **does** exist, is populated on 61,157 posted entries, and reaches **no** entry's full item set | `CONTRADICTED — CORRECTED` | **P07** | `CO` | **YES** | `49` §3 |
| `HO-04` | CANDIDATE HANDOFF | **Correction to a P08 claim two peers built on:** the accounting-event absence is **withdrawn**; identity exists per channel, is not a platform property, and is unpopulated | `CONTRADICTED — CORRECTED` | **P09, P10** | `PLAT` | **YES** | `48` §2.2 |
| `HO-05` | CANDIDATE HANDOFF | Relocation is **not** bounded by the absence of a lock — it is the default for every non-sale document | `FACT VERIFIED — P08` | **P04, P06, P10** | `CO` | **YES** | `46` §6 |
| `HO-06` | CANDIDATE HANDOFF | The posting state sits **outside** the integrity seal's field set | `FACT VERIFIED — P08` | **P05** | `PLAT` | **YES** | `48` §3 |
| `HO-07` | CANDIDATE HANDOFF | A raw-statement write of an accounting field bypassing the guard layer. **CORRECTED `P08-CONTRA-72`: it is NOT in the accounting core** — it lives in a separate accountant module, which matters to the consumer who must find it. **And its reachability was measurable and unmeasured:** the module is installed on all three databases, the triggering field is null on all 89 companies, and 0 entries carry the affected state — **reachable everywhere, unengaged by configuration, one field-write from firing across every posted entry before that date** | `FACT VERIFIED — P08` | **P06** | `PLAT` | **YES** | `43` |
| `HO-08` | CANDIDATE HANDOFF | **Version boundary:** every P08 source statement is 18.0; every deployed count is 16.0 or 19.0; **no deployed database matches the source line** | `FACT VERIFIED — P08` | **all peers, P11** | `PLAT` | **YES** | `40` |
| `HO-09` | CANDIDATE HANDOFF | **Denominator correction, itself corrected (`P08-CONTRA-65`):** a **preventive** control's denominator is **capability**, not history — **7 of 89 companies, 75 of 109 journals**. Platform (89/109) and history (6/29) retained and labelled | `CONTRADICTED — CORRECTED` | **all peers, P11** | `PLAT` | **YES** | `53` CQ-10 |
| `HO-10` | CANDIDATE HANDOFF | **CORRECTED `P08-CONTRA-53`.** The **declared** root set is **22**. Class-`A` negatives were expressed over the subset carrying each pattern (21, or 20 for the core posting file) and the surface published `N of 21` without saying so. **Independence is the binding limit: the core posting file resolves to 7 distinct contents by hash** | `FACT VERIFIED — P08` | **P09, P10, P11** | `PLAT` | **YES** | `48` §3 |
| `HO-11` | CANDIDATE HANDOFF | **19 Boss decisions**, none answered, including one **CONTESTED** invariant | `BOSS DECISION REQUIRED` | **Boss** | `PLAT` | no — Boss-direct | `52` §4 |
| `HO-12` | CANDIDATE HANDOFF | `AAS+-VETO-01` — two conditions gating reliance on any P08 finding | `BOSS DECISION REQUIRED` | **Boss, PMO** | `PLAT` | no — Boss-direct | `50` §4 |

---

## 5. Counts

| | |
|---|---|
| **CANDIDATE INPUT** | **11** |
| **PROCESS** | **10** |
| **CANDIDATE OUTPUT** | **9** |
| **CANDIDATE HANDOFF** | **12** |
| Items naming a candidate producer/consumer **without researching it** | **17** |
| Items carrying an open dependency | **20** |
| Items labelled a final contract | **0** |


---

## 6. Corrections applied after the bounded AAS-03 challenge

### 6.1 `IN-08` — the tax-period claim, decomposed on the population the mechanism can act on

**`P08-CONTRA-58`.** The published headline — *"0 of 61,157 entries propagate the tax period to their full item set"* — is arithmetically exact and uses a **unit the deployed mechanism never attempts**. It stamps **tax lines only**. Decomposed on that eligible population:

| Of the 61,157 posted entries carrying an entry-level tax period | Entries | Share |
|---|---|---|
| **No tax line at all — nothing the mechanism could stamp: INELIGIBLE** | **33,190** | **54.3%** |
| **Every tax line stamped — the mechanism worked as written** | **18,123** | **29.6%** |
| **Has tax lines, none stamped — the real defect** | **9,829** | **16.1%** |
| Partially stamped | 15 | — |

**The published framing inverted the severity.** The defect population is **16.1%**, not 100%.

**And the consequence clause is refuted.** `57` §2 stated *"nothing that reads the item can tell."* The deployed statutory register reads the **entry** carrier through a join that falls back to the item's accounting date. The thing that reads the item **can** tell.

**This is the same eligibility defect the author caught in `CQ-P08-10` — committed again, in the same round, in a different file.** `P08-M-19`.

### 6.2 New candidate inputs the `move_type` partition concealed

The five-way partition of `53` CQ-01 is **documentary**, so 76.6% of the posted ledger falls into one residue bucket described as *"no document behind it."* At least these arrive through it and are now named:

| Candidate input | Measured (`D16`, posted) |
|---|---|
| Payment-originated entry | 21,593 |
| Statement-originated entry | 13,267 |
| Reversal as an arrival | 5,057 |
| Cash-basis tax entry | 7,701 |
| Kernel-generated exchange difference | 3,169 |
| **Scheduler-posted entry** — posted by an unattended job, no user act at the moment of posting | **8,118**, all asset-linked |
| Memo / non-monetary display rows inside the item set | 881 items |
| Analytic-bearing item | **338,400 of 417,700 — 81.02%** |

`P08-CONTRA-60`. **The Candidate INPUT inventory is a floor, not a census, and its partition was the cause.**

### 6.3 A boundary actor with no category in this pack

**`P08-CONTRA-55`.** A module **installed in all three deployed databases** deletes the settlement, item and entry tables in unqualified raw SQL and resets the entry-number sequence to 1. It is **neither an input nor an output** — it is a **boundary actor that destroys ledger facts**, and this pack has no category for it. Recorded here pending one, and handed to **P11** and **P06**.

### 6.4 `P08-F-51` — the two tax-period carriers contradict each other on 24.2% of the items where both are set

**Found independently by two challengers and re-run by the author. All three agree to the row.**

| Posted items where both the entry stamp and the item stamp are set | Items |
|---|---|
| The two **agree** | 13,764 |
| **The two DISAGREE** | **4,393 — 24.2%** |
| — disagreeing by **month** | **747** |
| An item carries a stamp its entry does not | 4 |

The deployed mechanism writes the entry's value onto the tax lines **at create**, so the two copies **agree at birth**. A 24.2% divergence is therefore evidence of one copy being changed without the other — and the field carries no change tracking and sits outside the integrity seal's set.

**This is a sharper instance of the package's own central thesis than the one it published.** A *partially and inconsistently* stamped entry is worse for any period-based selection than an unstamped one, because an item-level selection returns one subset and an entry-level selection returns a different one. **747 of these fall in different months.**

**The author does not attribute the divergence to post-create mutation as a verified fact.** A challenger tested a mutation discriminator and reported it **failed to discriminate** (100.0% vs 98.8%), and reported the failure. Identifying the writer needs an audit source outside the current path set. `SUPPORTED INTERPRETATION — P08` for the mechanism; **`FACT VERIFIED — P08` for the divergence itself.**

### 6.5 `P08-F-52` — the entry-number mirror is stale-empty, not corrupt

`PR-10` publishes **174,977** disagreeing mirrors. A challenger decomposed it and the author re-ran the decomposition:

| | Items |
|---|---|
| Mirror **unpopulated** (null or the draft placeholder) while the entry carries a real number | **174,959** |
| Mirror **genuinely pointing at a different, wrong number** | **18** |

**And those 18 are exactly the deleted-entry residue already recorded in `CQ-P08-06`.** So the mirror fails by being **empty**, never by being **wrong**, except at the 18 items that already have their own finding. `PR-10`'s bare "174,977 disagree" invites the stronger and incorrect reading, and is corrected here.
