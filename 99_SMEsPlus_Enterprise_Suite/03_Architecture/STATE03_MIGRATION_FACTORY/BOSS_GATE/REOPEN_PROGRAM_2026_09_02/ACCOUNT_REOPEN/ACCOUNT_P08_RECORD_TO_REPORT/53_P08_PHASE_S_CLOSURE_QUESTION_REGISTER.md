# P08_PHASE_S_CLOSURE_QUESTION_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · baseline `838134f` · **PHASE S — DOMAIN PURITY FIRST**

Twelve bounded questions. **No question is answered by re-running closed work.** Each states its evidence, its version and database scope, and terminates in a permitted disposition. **AI EOS OFF. No design. No PHASE SA. No P11 architecture.**

**Version discipline, carried on every row.** Source observations are the **18.0** reference line unless stated. Deployed counts are **`DB-SM` 16.0**, **`DB-BK` / `DB-EV` 19.0**. **No deployed database matches the source line.** A source fact and a deployed count are never combined into one fact.

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

**The interface fact P08 owns:** the ledger accepts an entry **without requiring provenance**, and provenance density varies by class from **26.8% to 100%**. The purchase-side class — the largest documentary class — arrives with the **weakest** provenance of all.

**P08 does not investigate why any producer emits an entry that way.** `EXTERNAL DOMAIN BOUNDARY — DO NOT RESEARCH HERE.`

**Minimum identity guaranteed at the boundary:** company, journal, accounting date, posting state, and — **only once posted** — an assigned number. **Nothing else is guaranteed.** No durable event key, no producer identity, no mode marker.

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
| Whether the deployed derivation preserves collision-freedom | not assessed | `UNRESOLVED — SPECIFIC P08 EVIDENCE UNAVAILABLE` |

**The finality claim P08 can defend:** posting assigns a number and changes a state. **It does not make the entry immutable, and nothing in the measured surface makes it so** — the seal is off everywhere it could have been on, and the state it would protect is outside what it covers.

**Disposition: `FACT VERIFIED — CLOSED`, with one named `UNRESOLVED`.**

---

## CQ-P08-04 — Dates / Period / Close

| Fact | Class |
|---|---|
| The accounting date of a **non-sale** document is **system-derived from the document date with no lock involved**; sale documents are exempt | `FACT VERIFIED` — 18.0 source |
| Divergence between accounting date and document date: **20.95%** of purchase entries against **0.12%** of sale entries — a 175× asymmetry matching the exemption | `FACT VERIFIED` — 16.0 data |
| That the mechanism **caused** the 2,123 forward divergences | `SUPPORTED INTERPRETATION — P08` — ~100% carry one of its two signatures; 16.0 source not read |
| What produced the **5,622 backward** divergences | `UNRESOLVED — SPECIFIC P08 EVIDENCE UNAVAILABLE` |
| **There is no accounting-period object.** A period is a date range on a company record | `FACT VERIFIED` — 22 of 22 roots, with the independence caveat of CQ-12 |
| A posting aimed at a locked period is **relocated, not refused** — including under the irrevocable lock, asserted by the product's own test | `FACT VERIFIED` — 18.0 source |
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
| **6,585** posted entries (3.9%) carry no origin pointer of any kind; 2,617 of those carry no reference text either | `FACT VERIFIED` — corrected from 83,820, `48` §1 |
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
| — its measured consequence | **4 posted entries**, all from a **1:1 rate fallback**; the other 49 previously counted carry a legitimate company-currency counter-leg | `CONTRADICTED — CORRECTED AND CLOSED` |
| Account code uniqueness | enforced in 16.0; **the 19.0 schema has neither a company column nor a code column** — the claim is **not formulable** there | `FACT VERIFIED` (16.0) / `UNRESOLVED` (19.0) |
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
| **The deployed estate adds a custom reporting module this bound does not cover** | `UNRESOLVED — SPECIFIC P08 EVIDENCE UNAVAILABLE` |
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

| | Published | **Transacting only** |
|---|---|---|
| Companies | 89 | **6 — 6.7%** |
| Journals | 109 | **29 — 26.6%** |
| Period lock set | 0 of 89 | **0 of 6** |
| Tamper seal set | 0 of 109 | **0 of 29** |

> **`P08-CONTRA-43`. "0 of 89 companies" and "0 of 109 journals" were measured over a population that is 93% empty shells. A control unconfigured on a company that has never posted is evidence of nothing.**

**The corrected claim is smaller and much stronger: every company and every journal that has ever posted an accounting entry has the seal off and the lock unset — 0 of 6 and 0 of 29, with no exception.**

This is the eligibility defect the programme has recorded before: the four denominator clauses all assume the set is eligible, and eligibility was not tested.

| Further scope fact | Class |
|---|---|
| PLATFORM / TENANT / COMPANY separation as the governing model | `FACT VERIFIED` — CORR1 adopted |
| A posted entry in another company's journal | `FACT VERIFIED` — deployed |
| Ledger accounts posted to by more than one company | `FACT VERIFIED` — 3 accounts in `DB-BK` |
| A statutory register query with **no company predicate**, installed on two 44-company databases | `FACT VERIFIED`, **and not yet carried into the scope matrix** |
| Cross-company settlement | **0 of 63,779** — but the multi-company databases hold 22 posted entries between them, so the test is **near-uninformative** | `FACT VERIFIED` within the evidence set, **`B` for the estate** |

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
| **Named `UNRESOLVED` items, each with a specific evidence requirement** | **4** — deployed numbering collision-freedom; the 5,622 backward date divergences; account uniqueness not formulable in the 19.0 schema; the deployed reporting module |
| **Standing integrity limits** (a different unit — do not add these to the row above) | **3**, listed below |
| `BOSS DECISION REQUIRED` | **19**, none answered — **enumerated, not asserted**; the published total of 18 was wrong (`P08-CONTRA-45`) |
| `EXTERNAL DOMAIN BOUNDARY` routed to a named owner | **12** |
| Terminal items with no owner and no next action | **0** |

**Three integrity limits P08 publishes against itself:**

1. **`N of 21 roots` is at most 7 independent observations** — the core posting file resolves to 7 distinct contents by hash. Every root-set negative overstates its support roughly threefold.
2. **Predicate risk is unretired.** Three of eleven published predicates were wrong and **all three passed a positive control**. `AAS+-VETO-01` C-1 requires every measurement re-issued with its predicate in executable form; **that is not discharged.**
3. **`P08-U-18` is open at 15 modules**, reduced from 32. Two sit under class-A claims; one is a customization container able to carry arbitrary models and server-side automation.

**Disposition: `UNRESOLVED — SPECIFIC P08 EVIDENCE UNAVAILABLE` for the three limits, each with a named next action. No unbounded search remains.**
