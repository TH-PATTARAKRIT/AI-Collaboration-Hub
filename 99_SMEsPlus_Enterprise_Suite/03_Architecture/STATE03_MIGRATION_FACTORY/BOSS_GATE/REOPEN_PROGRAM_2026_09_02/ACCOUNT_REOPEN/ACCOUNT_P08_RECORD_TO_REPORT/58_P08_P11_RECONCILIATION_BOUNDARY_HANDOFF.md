# P08_P11_RECONCILIATION_BOUNDARY_HANDOFF

Prompt `[SMEPLUS-26-09-06-P08-R2R-DOMAIN-PURE-BOUNDED-CLOSURE-002]` · **PHASE S** · answers `CQ-P08-09`

> **P08 states what the ledger can and cannot supply to a reconciliation. P08 does NOT define the reconciliation architecture. Every item is a CANDIDATE awaiting PHASE B.**

---

## 1. What P08 can supply

| # | Supplied | Quality | Class |
|---|---|---|---|
| 1 | Every posted monetary fact, at item granularity | **complete and arithmetically sound** — 0 unbalanced posted entries in the reporting currency across 169,143 | `CANDIDATE OUTPUT` |
| 2 | The settlement graph | **63,773 records, 100,580 lines, residual drift 0** at tolerance ≥ 1e-6 | `CANDIDATE OUTPUT` |
| 3 | Company and journal attribution on every item | mirrors agree **447,384 of 447,384** — *unit note: this is the all-states item population; the posted population is 417,700* | `CANDIDATE OUTPUT` |
| 4 | Posting state and date | present on every entry | `CANDIDATE OUTPUT` |
| 5 | Origin pointers where they exist | **96.1% of posted entries** carry at least one | `CANDIDATE OUTPUT` |

## 2. What P08 cannot supply, and why

**This is the more important half.**

| # | Not supplied | Why | Class |
|---|---|---|---|
| 1 | **An independent record to reconcile the ledger against** | for the party dimension there is none — the subledger **is** the ledger filtered by account, so agreement is **true by construction and unverifiable** | `FACT VERIFIED` |
| 2 | **A reconciliation obligation for the genuinely separate stores** | the asset register and the inventory valuation record **are** separate stores; **the kernel imposes no tie-out, no periodic proof and no exception** | `FACT VERIFIED` — `P08-RQ-KRN-01` |
| 3 | **An as-of reconstruction of any balance** | no bitemporal record; `amount_residual` is current state only | `FACT VERIFIED` |
| 4 | **A period to reconcile within** | there is **no accounting-period object** — a period is a date range on a company record | `A VERIFIED ABSENCE`, 7-observation limit |
| 5 | ~~A trustworthy settlement chronology~~ **WITHDRAWN — `P08-CONTRA-57`.** The as-of date is **computed by the accounting kernel** as the later of the two items' accounting dates. The 46.4%/44.3% split compared a system write timestamp against that derived date and **contains no defect** | — | `CONTRADICTED — CORRECTED` |
| 6 | **A durable event identity to reconcile on** | identity exists on **one** inbound channel, on a nullable column, **unpopulated on all 13,814 rows** | `FACT VERIFIED` — base narrowed in `48` §2.2 |
| 7 | **Provenance at the level a reconciliation would read** | 41.89% of items cannot name their entry; 17.00% carry no origin mark | `FACT VERIFIED` |
| 8 | **A closed period as a stable comparison basis** | close is a date comparison; **0 of 6 transacting companies** set one | `FACT VERIFIED` |

## 3. What P11 must decide — stated, not answered

| # | Question P11 owns |
|---|---|
| 1 | Whether reconciliation is a **derivation** over one ledger or a **comparison** between two independent records — the benchmark makes the first structurally unavoidable for the party dimension |
| 2 | What a control-account tie-out means when the subsidiary record is the same rows |
| 3 | How a reconciliation is expressed **as of** a date when no as-of reconstruction exists |
| 4 | Whether the failure of a tie-out is itself an accounting event |
| 5 | How two Pxx truth sets are compared at all — **`EXTERNAL DOMAIN BOUNDARY — ROUTE TO P11 / PHASE B`** |

**P08 answers none of these and offers no preferred option.**

## 4. Boundary discipline observed

- P08 did **not** open P11's package, define its architecture, or rank its options.
- P08 did **not** research any producer's lifecycle to characterise what it emits.
- Every peer-supplied fact used here is **attributed and marked as received**, never restated as P08's own.
- **`AAS+-VETO-01` applies to this handoff.** No item here may be relied upon for design until its two conditions are met.

**Disposition: `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED`.**


---

## 5. Correction after the bounded AAS-03 challenge — a destroyer of reconcilable facts

**`P08-CONTRA-55`. The single most consequential omission from this handoff.**

A module **installed in all three deployed databases** deletes, in unqualified raw SQL and in this order: the **settlement table**, then the **journal item table**, then the **journal entry table** — with **no company predicate, no state predicate, a commit after each table**, and a reset of the entry-number sequence to **1**.

| Consequence for P11 | |
|---|---|
| §1 item 2 offers the **settlement graph** as reconcilable | it is deletable outside the object layer |
| §1 items 1 and 4 offer **posted facts and their state** | posted entries are removed exactly as drafts are |
| `56` §2 ranked settlement referential integrity as the one control that **holds** | it does not |
| `PR-04` entry numbering | a sequence reset permits previously-issued numbers to be re-issued |

**Handed to P11 and to P06 as `HO-13`.** P08 records the mechanism and the install state. **Whether it has ever been executed on any deployment is not verified by P08** — a peer has published an observation to that effect and it is recorded as **received and attributed, not re-derived**.

## 6. Handoffs added after challenge

| ID | To | Content |
|---|---|---|
| `HO-13` | **P11, P06** | the deletion path above |
| `HO-14` | **P07** | the statutory register family selects on **two different period bases** — two handlers on the tax period, two on the accounting date — so the 5,228 entries where the two differ can appear in one and not the other |
