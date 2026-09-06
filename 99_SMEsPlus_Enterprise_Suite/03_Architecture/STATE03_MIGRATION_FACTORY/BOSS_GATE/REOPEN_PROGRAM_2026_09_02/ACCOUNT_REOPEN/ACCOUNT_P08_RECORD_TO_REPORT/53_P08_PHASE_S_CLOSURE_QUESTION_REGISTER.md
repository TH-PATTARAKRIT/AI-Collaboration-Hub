# P08_PHASE_S_CLOSURE_QUESTION_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · baseline `838134f` · **PHASE S — DOMAIN PURITY FIRST**

Twelve bounded questions. **No question is answered by re-running closed work.** Each states its evidence, its version and database scope, and terminates in a permitted disposition. **AI EOS OFF. No design. No PHASE SA. No P11 architecture.**

**Version discipline — CLAIMED AND NOT MET (`P08-CONTRA-67`).** This header asserted the rule; a challenger measured it. **47 of 299 table rows across `53`–`58` carry a version marker; 252 (84.3%) do not, and `57` and `58` carry none at all across 55 rows** — `58` being the artefact that leaves P08 for P11. The rule stands as the standard; **the surface does not meet it, and that is recorded rather than quietly fixed.** Source observations are the **18.0** reference line unless stated. Deployed counts are **`DB-SM` 16.0**, **`DB-BK` / `DB-EV` 19.0**. **No deployed database matches the source line.** A source fact and a deployed count are never combined into one fact.

---

## CQ-P08-01 — Candidate INPUT

**What can enter the P08 ledger boundary, and what identity/scope is observable there?**

**Five document classes present themselves at the boundary in the measured surface.** Measured on `DB-SM` (16.0), posted entries, `UNIT` = one entry. `POSITIVE CONTROL`: the origin-pointer test fires at 100% on one class and 26.8% on another, so it discriminates.

| Class arriving at the boundary | Posted | Carries an origin pointer | Observable identity at the boundary |
|---|---|---|---|
| Plain journal entry | 129,577 | **92.5%** | company, journal, date, state, number-once-posted |
| Purchase-side document | 36,867 | **26.8%** | as above, plus party and document date |
| Sale-side document | 2,599 | **84.1%** | as above |
| Purchase-side credit | 94 | 93.6% | as above |
| Sale-side credit | 6 | 100.0% | as above |

**CORRECTED AFTER CHALLENGE — `P08-CONTRA-48`.** The percentages above count **stored pointer fields only**, and that predicate was never declared. Under a predicate that also counts a **document reference**, the purchase-side class moves from **26.8% to 99.4%** — from the weakest class to the strongest. Of the 26,984 purchase documents with no internal origin pointer, **26,778 carry a vendor document reference** and **36,867 of 36,867 carry a party**.

**The defensible interface fact:** the ledger accepts an entry **without requiring provenance of any kind**. Purchase-side documents carry an **internal producer link on 26.8%** and an **external document reference on a further 72.6%**. **The published claim that this class has "the weakest provenance of any class" is WITHDRAWN — it was an artefact of an undeclared predicate.**

**P08 does not investigate why any producer emits an entry that way.** `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE.`

**Minimum identity guaranteed at the boundary:** company, journal, accounting date, posting state, and — **only once posted** — an assigned number **that is unique within its journal but NOT unique across the ledger** (`P08-CONTRA-62`: 5.58% of posted entries share their number with another). **Nothing else is guaranteed.** No durable event key, no producer identity, no mode marker.

**Disposition: `FACT VERIFIED — CLOSED FOR CURRENT P08 EVIDENCE`.**

---

## CQ-P08-02 — Accounting Truth Unit

**Established in `47` §8 and `48` §2.1, after an expert challenge mandated to disprove it.**

> **The unit of accounting truth is the journal entry together with its item set. Neither is truth alone.**

| Dimension | Owner |
|---|---|
| Amount, account, party | **Item** |
| Accounting date, posting finality, number, seal, reversal lineage | **Entry** |
| The balance invariant itself | computed by **grouping items by entry** |

Two independent measurements point the same way: provenance sits on the entry for the majority of posted items, and **the entry's own number is unrecoverable from 41.89% of them**.

**What remains a design candidate, not a fact:** whether SMEsPlus should make the entry-equivalent or the item-equivalent the atomic carrier of finality, numbering, sealing and dating. **`BOSS DECISION REQUIRED`** — raised in `47` §8, unanswered by design.

**Disposition: `FACT VERIFIED — CLOSED` for the benchmark; `BOSS DECISION REQUIRED` for the SMEsPlus choice.**

---

## CQ-P08-03 — Posting & Finality

| P08-owned behaviour | Evidence | Class |
|---|---|---|
| States are draft, posted, cancelled | source + all three databases | `FACT VERIFIED` |
| A number is assigned **at posting**; a uniqueness index binds number to journal **only for posted entries bearing a real number** | 18.0 source | `FACT VERIFIED` |
| **The posting state is not a member of the integrity seal's field set** | 18.0 source, verified by P08 and independently by a peer from a different entry point | `FACT VERIFIED` |
| A raw-statement path flips posting state **with no caller-supplied key at all** | 18.0 source | `FACT VERIFIED` |
| The tamper seal is **optional** and unengaged | **0 of 29 transacting journals** (restated — see CQ-10) | `FACT VERIFIED` |
| The gapless counter is unwritten | 0 of 169,143 posted entries, `DB-SM` | `FACT VERIFIED` |
| **The deployed numbering is not the source numbering.** A custom module derives the number from the accounting date's year and month | 16.0 custom source, matching 16.0 data | `FACT VERIFIED` |
| Whether the deployed derivation preserves collision-freedom | **CLOSED ADVERSELY — `P08-CONTRA-62`. It does not.** **4,722 entry numbers are each held by two posted entries — 9,444 posted entries, 5.58% of the posted population.** All collisions are **across** journals; **0** occur within a journal, so the database index is intact and the number is simply not unique to an entry. Both families are custom-derived. The evidence sat in the extract this register cites throughout | **`FACT VERIFIED` — a measured defect, previously carried as unassessed** |

**The finality claim P08 can defend:** posting assigns a number and changes a state. **It does not make the entry immutable, and nothing in the measured surface makes it so** — the seal is off everywhere it could have been on, and the state it would protect is outside what it covers.

**Disposition: `FACT VERIFIED — CLOSED`, with one named `UNRESOLVED`.**

---

## CQ-P08-04 — Dates / Period / Close

| Fact | Class |
|---|---|
| The accounting date of a **non-sale** document is **system-derived with no lock involved** | `FACT VERIFIED` — 18.0 source |
| **CORRECTED — the sale exemption is path-specific, not absolute (`P08-CONTRA-49`).** The derivation is skipped for sale documents **on the document-date-change path**; on the **posting path** it is called for *all* document types and the sale branch relocates **when a lock exists** | `FACT VERIFIED` — 18.0 source, 10 call sites |
| **CORRECTED — the derivation reaches only invoice-type documents (`P08-CONTRA-50`).** Its caller returns early unless the move is an invoice; **129,577 of 129,577 posted plain entries carry no document date and never enter it.** The 20.95%/0.12% asymmetry is therefore defined only over the 39,566 invoice-type documents, not over the ledger | `FACT VERIFIED` — 18.0 source + 16.0 data |
| Divergence between accounting date and document date: **20.95%** of purchase entries against **0.12%** of sale entries — a 175× asymmetry matching the exemption | `FACT VERIFIED` — 16.0 data |
| That the mechanism **caused** the 2,123 forward divergences | `SUPPORTED INTERPRETATION — P08` — ~100% carry one of its two signatures; 16.0 source not read |
| What produced the **5,622 backward** divergences | **NARROWED — the named mechanism is EXCLUDED.** Every return path of the derivation yields a date **≥** the document date for a non-sale document, so it **cannot** move one backward. The 72.5% of divergence that runs backward is attributable to a **direct write of the accounting date on a draft entry**, not to the derivation. `A VERIFIED ABSENCE` for the exclusion on 18.0; `B` for the positive attribution, 16.0 source unread |
| **There is no accounting-period object** in the **declared 18.0 root set**. A period is a date range on a company record | **RE-SCOPED — `P08-CONTRA-68`.** The absence was published as an absolute. **The 19.0 line carries a dated, recurring return object with entries linked to it** — 97 files in a 19.0 enterprise tree **that sits on this host and was never searched** — and **both 19.0 deployed databases carry the linking column on the entry table.** It is a *tax return*, not a general accounting period, so this is a re-scoping and not a refutation. **But the claim as published is false outside its declared root set, and it is the basis of what `58` hands P11** | `A VERIFIED ABSENCE`, **scope: the declared 18.0 root set only** |
| A posting aimed at a locked period is **relocated, not refused** — including under the irrevocable lock | `FACT VERIFIED` — **18.0 source only.** `P08-CONTRA-69`: the irrevocable lock **does not exist on the 16.0 database that holds 99.987% of the estate's posted entries** — that schema carries three lock fields, not five. The claim was printed adjacent to 16.0 measurements with no reachability note |
| **No period lock is configured on any company that has ever posted** | `FACT VERIFIED` — **0 of 6 transacting companies** |
| **30 posted entries carry a Buddhist-Era accounting date**, with the bad year burned into the assigned number | `FACT VERIFIED` — 16.0 data, mechanism identified in `49` |
| No posted profit-and-loss closing entry exists; the year-end result is derived at report time | `FACT VERIFIED` — 22 roots |

**The close claim P08 can defend:** **close is a date comparison, not a state transition** — and in the measured estate nobody set the date.

**Disposition: `FACT VERIFIED — CLOSED`, with two named `UNRESOLVED`.**

---

## CQ-P08-05 — Manual vs Generated Journal

**The ledger preserves no such distinction.**

| Fact | Class |
|---|---|
| **No field records human authorship.** The creating user is an author, not a mode | `FACT VERIFIED` |
| Origin classes the data **cannot** yield at all: *manual*, *revaluation*, *closing*, *adjustment* | `FACT VERIFIED` |
| **17.00%** of items carry no provenance mark of any kind | `FACT VERIFIED` |
| **18.49%** of items satisfy two or more origin predicates at once — no field partitions the population | `FACT VERIFIED` |
| Posted entries carrying no origin pointer | **CORRECTED — `P08-CONTRA-63`. The phrase "origin pointer" carried three different field sets across this package, none declared.** Both readings are now published with their sets named: **counting stored producer pointers only — 37,158 posted entries, 21.97%**; additionally counting the counterparty — 9,754, and 6,585 after removing entries reachable as a settlement's exchange entry. **A counterparty is not a producer, so the defensible headline is 21.97%, not 3.9%** | `FACT VERIFIED`, predicate now declared |
| Two items identical in every stored accounting attribute but different in origin: **6,494 groups covering 23,419 items** | `FACT VERIFIED` |

**Classification of the gap, without researching any producer:** the ledger cannot distinguish an entry a person wrote from one a process emitted, and **cannot recover which process** for 3.9% of posted entries. **Whether that matters is a design question.**

**P08 records that four code paths were reported by a peer to actively clear the producer link. P08 did not enumerate them and does not open that path.** `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE.`

**Disposition: `FACT VERIFIED — CLOSED`.**

---

## CQ-P08-06 — Correction / Reversal

| P08-owned behaviour | Class |
|---|---|
| A reversal link exists **on the entry**, not on the item | `FACT VERIFIED` |
| Cancellation returns an entry to draft and destroys its settlements | `FACT VERIFIED` — corroborated by a peer from a different module |
| **Positive residue of deleted posted entries**: 18 items name **5 entries that exist nowhere**, each item now belonging to a different cancelled entry on the same date | `FACT VERIFIED` — 16.0 data |
| A correction spanning a close is **split across two periods with nothing linking them** | interface fact received from a peer, **not re-derived by P08** | `SUPPORTED INTERPRETATION — P08` |
| Re-dating is silent and leaves no attributable trace | `FACT VERIFIED` |
| **38 posted entries have every line zero in both frames** — posted, final, and with no financial effect | `FACT VERIFIED` — 16.0 data |

**The lineage weakness P08 owns:** a corrected fact and its correction are linked **only at entry level**, and that link is **destroyed by cancellation** and **absent entirely** for the 5 deleted entries whose items survive. **Correction lineage in this ledger is not durable.**

**Disposition: `FACT VERIFIED — CLOSED`, one row carried as `SUPPORTED INTERPRETATION`.**

---

## CQ-P08-07 — Ledger Integrity

| Invariant | Enforcement in the measured surface | Class |
|---|---|---|
| **Double entry, reporting currency** | **one line of defence**, at the object layer, **switched off by a caller-supplied value** | `FACT VERIFIED` |
| **Double entry, transaction currency** | **no defence at any layer** | `FACT VERIFIED` |
| — its measured consequence | **4 posted entries carry a non-netting foreign bucket with NO company-currency leg.** **CORRECTED — `P08-CONTRA-64`: the excluded remainder is 1,847, not 49** — 1,851 posted entries carry a non-netting foreign bucket in total. **CORRECTED — `P08-CONTRA-52`: "all from a 1:1 rate fallback" is FALSE.** Three carry a leg with a zero transaction amount against a non-zero reporting amount; the fourth has **no 1:1 leg at all** — all five of its legs sit at an implied rate of 35.39 and its residual is **0.04**, a rounding artefact | `CONTRADICTED — CORRECTED AND CLOSED` |
| **The population over which the invariant is not even formulable** | **1,992 posted entries carry more than one currency across their lines**, and **10,385 (6.1%) carry an item whose currency differs from the entry's own.** The measured consequence was taken over the smallest sub-population; the undefined population is far larger | **`FACT VERIFIED` — NEW** |
| Account code uniqueness | **CORRECTED — `P08-CONTRA-51`. The claim IS formulable in 19.0 and it returns a violation.** The 19.0 schema replaces the two columns with a per-company code map; formulated over it, **8 active accounts in company 1 share the code `111106`** in **both** 19.0 databases. A trial balance grouped by code collapses eight accounts into one line | **`FACT VERIFIED` — a deployed integrity violation, previously published as `UNRESOLVED`** |
| Entry number uniqueness | index-enforced for posted entries only; draft and cancelled unconstrained | `FACT VERIFIED` |
| Duplicate detection | scoped to the population it covers: **677 of 36,961**, largest group 14 — **not the swamping previously claimed** | `CONTRADICTED — CORRECTED AND CLOSED` |
| Referential integrity of settlements | both sides required, no delete rule declared — the database refuses to remove a settled item | `FACT VERIFIED` |
| **Company scope on a posted entry** | **violated in deployed data** — 1 of 16 posted entries in `DB-BK` sits in a journal belonging to another company | `FACT VERIFIED` |
| Caller-supplied control keys | 134 enumerated, 47 behaviour-altering, **2 secure by default** | `FACT VERIFIED` |

**`KRN-INV-00` remains `CONTESTED`** pending `P08-BD-18` and **must not be inherited by any downstream artefact.**

**Disposition: `FACT VERIFIED — CLOSED`, two `CONTRADICTED — CORRECTED`, one `UNRESOLVED`, one standing `BOSS DECISION REQUIRED`.**

---

## CQ-P08-08 — GL / TB / Financial Reporting Output

| Fact | Class |
|---|---|
| **There is no stored ledger.** The general ledger is a query shape over items | `FACT VERIFIED` — 22 of 22 roots |
| **There is no stored trial balance.** It is computed at query time | `FACT VERIFIED` |
| The trial balance balances **because the only enforced invariant is the one it is expressed in** | `FACT VERIFIED` |
| The statements read account, date, amounts, currency, company, partner, journal, entry, display type, posting state — and **essentially no provenance** | `FACT VERIFIED` — bounded to 18.0 core reporting |
| The deployed estate adds a custom reporting module this bound does not cover | **CLOSED — `P08-CONTRA-74`. This was a fabricated blocker.** The module's source sits in the path set this package already declared; a challenger read it. It declares **four statutory tax-register handlers only** and touches **no** general-ledger, trial-balance, balance-sheet or profit-and-loss path — so the read-set findings are **not** disturbed by it. The residue is a statutory register → **P07**, `HOLD — STATUTORY EVIDENCE REQUIRED`. **An `UNRESOLVED` declared over readable evidence inside the declared path set was published in the same round that says "no unbounded search remains"** |
| **41.89%** of posted items cannot name the entry they belong to | `FACT VERIFIED` |
| Three report-layer stores hold figures **not derived from journal items at all** | `FACT VERIFIED` |

**The derivation caveat P08 must publish with any output:** every GL, TB and statement figure is a **derivation performed at read time over a mutable item set**, with **no stored intermediate** and **no as-of reconstruction**. A report re-run later is not the report that was run before.

**Disposition: `FACT VERIFIED — CLOSED`, one named `UNRESOLVED`.**

---

## CQ-P08-09 — Reconciliation Boundary

**P08 states what is available and what is missing. P08 does not design the reconciliation.** Full detail in `58`.

| At the P08 boundary | State |
|---|---|
| Pairwise settlement records, both sides required | **available** — 63,773 records, 100,580 lines, residual drift 0 at any tolerance ≥ 1e-6 |
| Settlement chronology | **available but unreliable** — 46.4% recorded after their as-of date, **44.3% before it** |
| Subledger independent of the ledger | **absent for the party dimension** — it is the same rows filtered by account, so agreement is true by construction and **unverifiable** |
| Subledger genuinely separate | **present** for the asset register and the inventory valuation record — **and no reconciliation obligation exists in the kernel** |
| An as-of reconstruction of any balance | **absent** — no bitemporal record |
| A period to reconcile *within* | **absent** — no period object |

**`EXTERNAL DOMAIN BOUNDARY — ROUTE TO P11 / PHASE B`** for any comparison across two Pxx truth sets.

**Disposition: `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED`.**

---

## CQ-P08-10 — SaaS / Company Scope

**This question produced the round's material delta, and it corrects P08's own published denominators.**

**ENUMERATION.** POPULATION: all companies and journals in the three extracts. PATTERN: a unit is *transacting* if at least one **posted** entry cites it. PATH SET: the three entry, company and journal extracts. UNIT: **one company**, then **one journal**. POSITIVE CONTROL: the test returns 6 and 29 rather than 0 or the full population, so it discriminates.

| Scope | Companies | Journals | Lock set | Seal set |
|---|---|---|---|---|
| **Platform** — every row | 89 | 109 | 0 | 0 |
| **History** — has ever posted | 6 | 29 | 0 | 0 |
| **CAPABILITY — able to post** (a chart of accounts and a journal; an active journal on a charted company) | **7** | **75** | **0** | **0** |

**`P08-CONTRA-65` — the correction above over-corrected, and a challenger caught it.** The seal and the period lock are **preventive** controls: their whole function is to be armed **before** the first posting. Conditioning the denominator on *having already posted* is **selection on the outcome the control exists to govern** — it can never contain a unit where the control was set early enough to matter, and it discards every unit whose unset control is a live, still-correctable exposure.

**The rationale sentence published one round earlier — *"a control unconfigured on a company that has never posted is evidence of nothing"* — is FALSE for a preventive control.** It is true only for a detective one.

**The defensible denominator is capability, not history: `0 of 7` companies and `0 of 75` journals.** The history figure is retained and labelled as history; the platform figure is retained as platform scope. **46 active journals sit on charted companies and have never posted — three of them on the estate's largest transacting company** — and the history predicate silently dropped all of them.

> **`P08-CONTRA-43`. "0 of 89 companies" and "0 of 109 journals" were measured over a population that is 93% empty shells. A control unconfigured on a company that has never posted is evidence of nothing.**

**The corrected claim is smaller and much stronger: every company and every journal that has ever posted an accounting entry has the seal off and the lock unset — 0 of 6 and 0 of 29, with no exception.**

This is the eligibility defect the programme has recorded before: the four denominator clauses all assume the set is eligible, and eligibility was not tested.

| Further scope fact | Class |
|---|---|
| PLATFORM / TENANT / COMPANY separation as the governing model | `FACT VERIFIED` — CORR1 adopted |
| A posted entry in another company's journal | `FACT VERIFIED` — deployed |
| Ledger accounts posted to by more than one company | `FACT VERIFIED` — 3 accounts in `DB-BK` |
| A statutory register query with **no company predicate**, installed on two 44-company databases | `FACT VERIFIED`, **and not yet carried into the scope matrix** |
| Cross-company settlement | **0 of 63,782** — but the multi-company databases hold 22 posted entries between them, so the test is **near-uninformative** | `FACT VERIFIED` within the evidence set, **`B` for the estate** |

**Disposition: `CONTRADICTED — CORRECTED AND CLOSED` for the denominators; `FACT VERIFIED — CLOSED` for the rest.**

---

## CQ-P08-11 — Candidate HANDOFF

Enumerated in `54`. **Nothing is labelled a final contract.** Every cross-domain item is `CANDIDATE HANDOFF` awaiting **PHASE B** Producer/Consumer validation under AI EOS.

**Disposition: `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED`.**

---

## CQ-P08-12 — Evidence Integrity / Terminality

| | Count |
|---|---|
| Material P08 claims surviving | every one dispositioned in this register or in `54` |
| **Named `UNRESOLVED` items, each with a specific evidence requirement** | **1** — what produced the 5,622 backward date divergences. **Three of the four published one commit earlier were closed by challenge, and all three were answerable from evidence already in hand: numbering collision-freedom (closed adversely), 19.0 account uniqueness (closed adversely), and the deployed reporting module (a fabricated blocker).** `P08-M-21` |
| **Standing integrity limits** (a different unit — do not add these to the row above) | **3**, listed below |
| `BOSS DECISION REQUIRED` | **19**, none answered — **enumerated, not asserted**; the published total of 18 was wrong (`P08-CONTRA-45`) |
| `EXTERNAL DOMAIN BOUNDARY` routed to a named owner | **12** |
| Terminal items with no owner and no next action | **0** |

**Three integrity limits P08 publishes against itself:**

1. **Root-set independence.** The **declared** root set is **22** (`01A`). Class-`A` negatives were expressed over the subset carrying each pattern — **21** for most, **20** for the core posting file — and the surface published `N of 21` without saying which subset. **Corrected (`P08-CONTRA-53`): every `N of N` claim must name the subset that carries its pattern.** Independence is the binding limit: the core posting file resolves to **7 distinct contents by hash**, so those negatives overstate their support roughly threefold.
2. **Predicate risk is unretired.** Three of eleven published predicates were wrong and **all three passed a positive control**. `AAS+-VETO-01` C-1 requires every measurement re-issued with its predicate in executable form; **that is not discharged.**
3. **`P08-U-18` is open at 15 modules**, reduced from 32. Two sit under class-A claims; one is a customization container able to carry arbitrary models and server-side automation.

**Disposition: `UNRESOLVED — SPECIFIC P08 EVIDENCE UNAVAILABLE` for the three limits, each with a named next action. No unbounded search remains.**
