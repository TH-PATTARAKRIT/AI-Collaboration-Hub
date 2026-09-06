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
| `IN-02` | CANDIDATE INPUT | The ledger effect of a purchase-side document | `FACT VERIFIED — P08` (D16: 36,867 posted, **26.8%** carry a pointer) | P01 / P05 | `CO` | document date proposed; **accounting date system-derived** | reversible; cancellation destroys settlements | `53` CQ-01, CQ-04 | **producer identity absent on 73.2%** — `EXTERNAL DOMAIN BOUNDARY` |
| `IN-03` | CANDIDATE INPUT | The ledger effect of a sale-side document | `FACT VERIFIED — P08` (D16: 2,599 posted, 84.1%) | P02 | `CO` | **exempt from date derivation** | as above | `53` CQ-01 | none |
| `IN-04` | CANDIDATE INPUT | A credit/refund ledger effect | `FACT VERIFIED — P08` (D16: 100 posted, 93.6–100%) | P01, P02 | `CO` | as its parent class | as above | `53` CQ-01 | none |
| `IN-05` | CANDIDATE INPUT | A settlement instruction pairing two ledger items | `FACT VERIFIED — P08` (D16: 63,773 records, 100,580 lines) | P06 | `CO` | **as-of date supplied by the producer**; 46.4% recorded after it, **44.3% before** | settlement is destroyed by cancelling either side | `53` CQ-09, `58` | **chronology is not trustworthy at the boundary** |
| `IN-06` | CANDIDATE INPUT | An asset lifecycle ledger effect | `FACT VERIFIED — P08` (D16: 17,513 posted entries carry an asset pointer) | P04 | `CO` | commonly **bulk-generated**; 6,306 arrived in a single catch-up | reversible | `47` §3, `48` §4 | **a separate register exists with no reconciliation obligation** |
| `IN-07` | CANDIDATE INPUT | An inventory valuation ledger effect | `FACT VERIFIED — P08` (D16: 56,589 posted entries carry a valuation pointer) | P03 / inventory | `CO` | at valuation event | reversible | `48` §1 | **separate store, no reconciliation obligation** |
| `IN-08` | CANDIDATE INPUT | A **tax-period stamp** arriving on the entry, distinct from the accounting date | `FACT VERIFIED — P08` (D16: **61,157 posted entries**, 5,228 differ from the accounting date, 1,316 by month) | P07 | `CO` | stamped at create | not maintained on correction | `49` §3 | **propagates to 0 entries' full item set** |
| `IN-09` | CANDIDATE INPUT | A currency rate applied to a foreign leg | `FACT VERIFIED — P08` | platform rate master | `PLAT`→`CO` | at post | — | `43`, `48` §4 | **a 1:1 fallback is reachable and produced 4 unbalanced entries** |
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
| `OU-01` | CANDIDATE OUTPUT | A posted, numbered journal entry | `FACT VERIFIED — P08` | all | `CO` | at post | reversible | `53` CQ-03 | **not immutable** — seal off, state unsealed |
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
| `HO-07` | CANDIDATE HANDOFF | A raw-statement write of an accounting field bypassing the guard layer **exists in the accounting core** | `FACT VERIFIED — P08` | **P06** | `PLAT` | **YES** | `43` |
| `HO-08` | CANDIDATE HANDOFF | **Version boundary:** every P08 source statement is 18.0; every deployed count is 16.0 or 19.0; **no deployed database matches the source line** | `FACT VERIFIED — P08` | **all peers, P11** | `PLAT` | **YES** | `40` |
| `HO-09` | CANDIDATE HANDOFF | **Denominator correction:** deployment claims must be read on **transacting** scope — 6 of 89 companies, 29 of 109 journals | `CONTRADICTED — CORRECTED` | **all peers, P11** | `PLAT` | **YES** | `53` CQ-10 |
| `HO-10` | CANDIDATE HANDOFF | The root-set independence limit: `N of 21` is at most **7** independent observations | `FACT VERIFIED — P08` | **P09, P10, P11** | `PLAT` | **YES** | `48` §3 |
| `HO-11` | CANDIDATE HANDOFF | **18 Boss decisions**, none answered, including one **CONTESTED** invariant | `BOSS DECISION REQUIRED` | **Boss** | `PLAT` | no — Boss-direct | `52` §4 |
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
