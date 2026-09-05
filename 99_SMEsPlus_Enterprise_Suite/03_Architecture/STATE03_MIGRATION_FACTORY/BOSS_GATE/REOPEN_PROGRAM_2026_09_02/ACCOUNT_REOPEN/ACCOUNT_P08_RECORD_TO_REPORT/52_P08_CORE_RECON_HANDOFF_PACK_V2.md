# P08_CORE_RECON_HANDOFF_PACK_V2

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-TFINAL`

**Supersedes `25_P08_CORE_RECON_HANDOFF_PACK.md`.** Recipients: **P11 Core Accounting Reconciliation**, the peer processes P01–P10, and the Boss.

> **Handed over under `AAS+-VETO-01`.** This pack is usable for **deciding what must be closed**. It is **not** a basis for design reliance until the veto's two conditions are met. Every element below states its own standing.

---

## 1. The answer to the mandated question

**What is the accounting source of truth?**

| Dimension | Where truth lives | Standing |
|---|---|---|
| **Monetary decomposition** — amount, account, party | **The journal item** — sole store, database-integral, arithmetically consistent | `FACT VERIFIED` |
| **Accounting standing** — recognition date, posting finality, number, seal, correction lineage | **The journal entry.** The balance invariant itself is computed by grouping items **by entry** | `FACT VERIFIED` |
| **Economic meaning** — what event this is, what produced it, original or derived | **Split** between entry, item, and nothing at all | `FACT VERIFIED` |
| **Event identity** | **The business record, per channel** — absent as a platform property | `FACT VERIFIED`, base narrowed |

> **The atomic unit of accounting truth is the journal entry together with its item set. Neither is the source of truth alone.**

Two independent measurements point the same way: **provenance sits on the entry for the majority of posted items**, and **the entry's own number is unrecoverable from 41.9% of them**.

**Whether SMEsPlus should therefore attach finality, numbering, sealing and dating to the entry-equivalent is a `DESIGN CANDIDATE` and belongs to P11 and the Boss.** P08 states the evidence and stops.

## 2. The seven breaks in the source-to-report chain

| # | Break | Class | Measured |
|---|---|---|---|
| 1 | **No durable event identity as a platform property** | `FACT VERIFIED` | identity exists on one inbound channel, on a nullable column, **0 of 13,814 rows populated** |
| 2 | **Provenance sits above the object the statements aggregate** | `FACT VERIFIED` | entry-only for the majority; **17.00%** carry none |
| 3 | **The enforced balance invariant is the reporting currency only** | `FACT VERIFIED` | mechanism verified; **measured harm is 4 entries**, all from a 1:1 rate fallback |
| 4 | **Close is a date comparison with no state** | `FACT VERIFIED` | no period object; **0 of 89 companies** configured |
| 5 | **Relocation is not gated on a lock at all** | `FACT VERIFIED` | **20.95%** of purchase entries diverge in a lock-free database, against **0.12%** of sales |
| 6 | **Subledger agreement is unverifiable by construction** | `FACT VERIFIED` | no independent record exists to disagree |
| 7 | **The statutory period dimension does not reach the item** | `FACT VERIFIED` | 61,157 entries carry a tax period; **0 propagate it to all their items** |

## 3. Controls present in source and unengaged in deployment — **seven instances**

**This is the package's central structural finding, and it survived four independent challenges.**

| Control | Deployed state |
|---|---|
| Tamper seal | **0 of 109 journals** |
| Period lock | **0 of 89 companies** |
| Audit retention | **present in the 19.0 estate, unset on 88 of 88 companies** |
| Event-identity keys | **0 of 13,814 rows** |
| Consistency-test module | **uninstalled in 3 of 3** |
| Gapless counter | **0 of 169,143 posted entries** |
| Statutory period carrier | **populated on 36.2% of entries, on 0% of their item sets** |

**A control nobody configures is equivalent to a control that does not exist.** Recorded as `P08-BD-17`.

## 4. Eighteen Boss decisions — none answered by P08

`P08-BD-01` … `P08-BD-18`, carried unchanged from `18` §4 with two added this round:

- **`P08-BD-18`** — does the kernel's balance invariant bind **per currency frame**, or only in the functional currency with a separate rate-consistency rule over monetary items? **`KRN-INV-00` is marked `CONTESTED` and must not be inherited downstream until this is answered.**
- **`P08-BD-16` sharpened** — a period lock that refuses would have **blocked a legitimate go-live migration** of 6,306 entries. The refuse-or-relocate question is not only about correction behaviour; it is about what a close control does to a lawful bulk load.

## 5. Outbound corrections peers must apply

**Two peers built on a P08 claim P08 has retracted.** Stated plainly so they do not discover it later.

| Peer | What must change |
|---|---|
| **P10** | Adopted *"no accounting-event object exists in any of the 22 roots"* and **relocated its central design element** on it. The claim is **withdrawn as `CONTRADICTED`**. P08's assessment is that P10's conclusion largely survives on the corrected fact — a per-channel key populated nowhere is still not a platform identity — **but it now rests on different and weaker ground and must be re-stated.** P08 does not re-classify a peer's finding |
| **P09** | Same claim underpins `H08-4` and the stated ground for a standing veto. Re-ground on: **identity exists per channel, is not a platform property, and is unpopulated** |
| **P10, P09** | The root-set constraint adopted from P08 (*"closed for only 3 of ~23 class-A claims"*) is **out of date in P08's favour** — but its replacement carries a new limit: **`N of 21 roots` is at most 7 independent observations** |
| **P07** | **P08's earlier answer was wrong.** A tax-period carrier **does** exist in the deployed system, populated on 61,157 posted entries, differing from the accounting date on 5,228 and falling in a different month on 1,316 — and **absent at item level on every one**. `X-11`, `X-12` and `P07-D-22` are answered on that corrected basis |
| **P04, P06, P10** | Relocation is **not** bounded by the absence of a lock. It is the default for every non-sale document. P08 supplies the deployed measurement none of them held |
| **P05** | P08 **independently verified** that the posting state sits outside the integrity seal — two packages, two entry points, one uncovered field |
| **P06** | P08 **independently confirms** input (5): a raw-statement write of an accounting-relevant field bypassing the guard layer **exists in the accounting core**, not only in the modules P06 examined |
| **All** | Every P08 source statement is **18.0**; every deployed count is **16.0 or 19.0**. **No deployed database matches the source line.** Any peer combining the two as one fact must re-read it as two facts with two scopes |

## 6. What P11 must reconcile that P08 could not

| # | Item | Owner |
|---|---|---|
| 1 | Whether the analytic dimension is a fact or an attribution | P09, Boss — `P08-BD-09` |
| 2 | How many measurement bases the kernel carries over one event set | Boss — `P08-BD-11` |
| 3 | Whether a period lock refuses or relocates, and what that does to a lawful migration | Boss — `P08-BD-16` |
| 4 | Whether the platform **requires** a period-control configuration | Boss — `P08-BD-17` |
| 5 | Whether the balance invariant binds per currency frame | Boss — `P08-BD-18`, `HOLD — STANDARD EVIDENCE REQUIRED` |
| 6 | Whether finality, numbering and sealing attach to the entry-equivalent or the item-equivalent | Boss — raised by `47` §8, unanswered by design |
| 7 | Which of the 22 reference roots SMEsPlus targets | Programme — `P08-BD-05` |
| 8 | The two intra-package contradictions whose resolution is a design position, not a fact | P11 — `P08-CONTRA-28` |

## 7. Open evidence P08 hands over rather than closes

| ID | Item | Class |
|---|---|---|
| `P08-U-18` | **15 installed modules unlocated on this host**, including a customization container able to carry arbitrary models and server-side automation — the residual route the context attack left open | **GATING** |
| `P08-U-19` | A statutory register query with **no company predicate**, installed on two 44-company databases | `FACT VERIFIED`, unincorporated |
| `P08-U-20` | The second statutory reporting stack, never examined | `C` |
| `P08-U-21` | What produced the **5,622 backward** accounting-date divergences | `UNRESOLVED` |
| `P08-U-22` | A fourth deployed database, declared unreadable by one tool and not retried with another | `C` |
| `P08-U-14`, `-15`, `-16`, `-17`, `-23` | Peer-handed instances, an unsearched settlement mechanism, a peer branch naming, a peer traversal, further trees | `C` / `B` |
| — | The correctly-scoped **successor** to the withdrawn class-A claim: *no accounting-event object with identity independent of the journal entry* | **UNTESTED across the root set** |

## 8. Standing

| | |
|---|---|
| **Terminal status** | **RECOMMEND HOLD** |
| **Exit criteria** | **0 of 8** |
| **Method convergence** | **NOT ACHIEVED** — 0 of 10 |
| **Tolerance-zero boundaries closed** | **0.** Two moved the wrong way; one is confirmed live and deployed |
| **Vetoes** | `AAS+-VETO-01` consolidated from four independent expert vetoes. **Not lifted** |
| **Artifact count** | 20 new (`33`–`52`), plus closure deltas on four registers and the quarantine index. **Merges named where mandated artifacts converged; the shortfall against 27 is recorded, not forced** |
| **Corrections this round** | **19, of which 0 were self-caught** |
| **Prohibited actions** | **None taken.** No production code, source, database, module, migration, configuration, deployment, release or merge. All runtime investigation read-only |
