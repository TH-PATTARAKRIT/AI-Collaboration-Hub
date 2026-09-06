# P10 — EVIDENCE POPULATION BOUNDARY  (`CQ-P10-12`)

Closure round `[SMEPLUS-26-09-06-G02-P10-TBR-BOUNDED-DEEP-CLOSURE-DESIGN-INPUT-001]`

**Terminal disposition: `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`, with the boundary declared and every dependent claim bounded to it.**

---

## 1. The Identity Ladder — applied, per P02's lesson

`Artifact != Snapshot != Database UUID != Database Lineage != Deployment Instance.`

P10's prior round conflated three of these rungs and was corrected. The corrected position:

| Rung | P10's count | Basis |
|---|---|---|
| **Artefacts** (files) | ≥ 23 archive files on this host | host-wide census, prior round |
| **Snapshots** (distinct point-in-time images) | 7 examined; more exist | — |
| **Database UUIDs** | **4 examined** | `ir_config_parameter` identity key |
| **Database lineages** | **3** — two of the four examined share one ancestor tenant; their company sets are **identical**, intersection 44 of 44 | prior round, corrected |
| **Deployment instances** | **UNKNOWN** | not determinable from archives alone |

**The company denominator follows the lineage rung, not the artefact rung: 46 distinct companies, not 90 company-rows.**

## 2. The Boundary as Declared for This Round

| Element | Declaration |
|---|---|
| **Population** | ~~The four deployed databases already examined~~ → **SIX distinct deployed databases; all six examined.** Corrected by execution, `G02-R-03` |
| **Selection unit** | One database UUID |
| **Path set** | Already declared and executed in the prior round; **not re-swept** |
| **Version boundary** | Deployed estate is **19.0+e on PostgreSQL 15** for the databases whose module manifests were read; the fourth line is an older generation |
| **Explicitly excluded** | Any further sweep. **This exclusion is the Constitution's monotonic-scope rule, not an evidence claim** |

## 3. Why This Is `UNRESOLVED` and Not `CLOSED`

Three facts, each of which alone prevents a universal denominator:

> ## CORRECTED BY EXECUTION — `G02-R-03`
>
> Both numbered grounds below were **wrong, in opposite directions**, and a peer had already issued the correction **naming P10**: *"P02 CORRECTS THE DENOMINATOR: there are 6 distinct archives and all 6 are readable with a newer database toolchain, which is installed. **P10's** and P01's evidence bases were bounded by the default binary."*
>
> 1. ~~*At least ten deployed databases exist; six were never examined.*~~ **Wrong unit.** Ten counted **artefacts**, including duplicate snapshots of one database. Keyed on the database, the distinct population is **six**. P10 over-stated the population and under-stated its own coverage in a single sentence.
> 2. ~~*A later snapshot exists on the host and could not be read — permission-refused.*~~ **CONTRADICTED.** It opens with an ordinary archive extractor. It is a plain-SQL web backup holding **44 companies, 563 journal items, zero deferral entries and zero lock dates**. A capability negative that was never re-tested — the fourth of this class in this programme.
>
> **All six distinct databases, plus the duplicate snapshot, have now been probed.**

| # | Archive | Companies | **Deferral entries** | Lock dates | Newly examined |
|---|---|---|---|---|---|
| A | Archive A | 44 | **0** | 0 | |
| B | Archive B | 44 | **0** | 0 | |
| C | Archive C | 1 | **0** | 0 | |
| D | Archive D | 1 | **0** | 4 | |
| E | Archive E | 1 | **0** | **4** | **YES** |
| F | Archive F | 1 | **0** | 0 | **YES** |
| G | Archive G | 44 | **0** | 0 | **YES** |

**Positive control on every zero.** the deferral-entry-to-source link structure exists as a table in all seven artefacts, each with a a data-block header and no data rows — **empty, not absent**. The byte-size control that cannot make that distinction is not relied on.

**What changes.** The lock-carrying population is **two** databases, not one — both snapshots of one deployment line, four locks each at `2026-02-28`; whether they are one company at two dates is `UNRESOLVED`. **What does not change:** the deferral mechanism has generated **zero entries in 6 of 6** distinct deployed databases. Correcting the denominator widened the support for `P10-F-G02-01` without moving its direction.

**Version basis, closed at schema level — `G02-R-04`.** Archive F is a plain-SQL dump of the **deployed 19.0+e** generation and carries its DDL. Measured there: the journal item carries the two window-date fields and **no recognition-period column** (71 columns); the journal entry carries the period-beginning date. **The collapse of recognition period into posting act, and its asymmetry against depreciation, hold on the generation the estate actually runs** — they are not artefacts of reading an older source tree.

**The standing caveat, now carried by every G02 deliverable:** *source claims are verified against generation 18.0+e; the field sets they turn on are verified present and unchanged in the deployed 19.0+e schema; behavioural equivalence is untested.*

## 3a. What Remains `UNRESOLVED`

1. **Behaviour on the deployed generation.** A schema is not a code path. No 19.0+e source tree was read, and admitting one would widen the round.
2. **Whether archives D and E are the same company at two dates.** Not established.
3. **P02 measured a database P10 has never examined** (`iErpOCC`, 2,564 invoiced-ahead lines). Under the monotonic-scope rule P10 **must not go and read it**. Its existence is nonetheless proof that P10's four are not the estate.

> **`P10-B-01` — no P10 statement about "the deployed estate" is a universal claim.** Every one is scoped to *the four databases examined, at the dates of their images*. Where a prior P10 document says "the estate", read "the four".

## 4. Negative-Claim Controls Carried Forward

| Negative claim | Denominator | Positive control | Failure control | Class |
|---|---|---|---|---|
| No deferral entry has ever been generated | the relation table of every database carrying the structure | sibling tables non-empty in the same extraction | **a data-block header present** — byte size alone cannot distinguish an absent table from an empty one | `A` within the four |
| One company row carries a period lock | 46 distinct companies / 90 company-rows | lock-family sibling column populated in every row | as above | `A` within the four |
| Three of four databases hold no assets, only templates | asset table, grouped by state | state column enumerated, not binarised | — | `A` within the four |
| The reference root contains no accounting-event model | one declared root, both trees | 216 hits for the sibling pattern | — | `A` within **one root**; the peer's 22-root claim is the peer's, at the peer's class |

**`Empty result != absence.` `Same zero != same cause.` `Installed != configured.` `Configured != exercised.`** All four are applied in the traces that follow, and the last is why §5 matters.

## 5. The Boundary's Sharpest Consequence for This Round

**The recognition mechanism P10 has spent five rounds on has never executed in any database P10 can read.** Zero deferral entries, four of four.

So every P10 finding about deferral behaviour is:

- **`FACT VERIFIED` about the code** — read directly, and in several cases confirmed by the product's own executed tests;
- **`INSTALLED AND CONFIGURED`** — the structures and all eight settings are present, and 43 of 44 companies in two databases are provisioned;
- **NOT `EXERCISED`** — no entry exists;
- therefore **NOT `ECONOMICALLY VALIDATED`** on any deployed data.

> **This is the single most important sentence in the closure round: P10 is designing from a mechanism the estate has installed, configured, and never used.** That is a strong position for a clean-room design input — nothing must be migrated — and a weak position for any claim about how the mechanism behaves in practice.

## 6. What P02's Population Adds That P10 Cannot Get Itself

P02's measurement — ~~*billing ahead of performance dominates, by roughly 17:1 and 10:1*~~ — is **WITHDRAWN by its author** (`G02-R-01`). The 17:1 ratio is the explicitly withdrawn one. On the posted basis the Archive C direction is **1.4:1 toward delivery**, and every other row is a **floor, not a measure**. It remains a fact about **revenue timing** obtained on a population P10 has not read.

**P10 consumes it as a controlled input and does not re-derive it.** Its consequence for P10 is stated at `CQ-P10-04` and `CQ-P10-10`, and the decision it implies is Boss-reserved.

## 7. Disposition

`CQ-P10-12`: **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`.**

The boundary is declared, the identity ladder is applied, the denominators are stated with their units, every load-bearing negative carries a control, and the unreadable and unexamined populations are named. **What is unavailable is a closed estate denominator, and obtaining it is forbidden to this round by the monotonic-scope rule** — not by lack of technique.

Owner of the residual: **P11**, as the process that owns cross-process population reconciliation. Handoff published.
